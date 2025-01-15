from data.init import curs
from errors import Duplicate, Missing
from model.explorer import Explorer

curs.execute("""create table if not exists explorer(
                name text primary key,
                country text,
                description text)""")


def row_to_model(row: tuple):
    (name, country, description) = row
    return Explorer(name=name, country=country, description=description)


def model_to_dict(explorer: Explorer) -> dict:
    return explorer.model_dump()


def get_one(name: str) -> Explorer:
    qry = "select * from explorer where name=:name"
    params = {'name': name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f'Explorer {name} not found')


def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


def create(explorer: Explorer) -> Explorer:
    qry = "insert into explorer values (:name, :country, :description)"
    params = model_to_dict(explorer)
    try:
        curs.execute(qry, params)
    except:
        raise Duplicate(msg=f'Explorer {explorer.name} already exist')
    return get_one(explorer.name)


def modify(explorer: Explorer) -> Explorer:
    qry = ('''update explorer 
                set country=:country,
                    name=:name,
                    description=:description,
                    area=:area
                where name= :name_orig''')
    params = model_to_dict(explorer)
    params['name_orig'] = explorer.name
    _ = curs.execute(qry, params)
    return get_one(explorer.name)


def replace(explorer: Explorer):
    return explorer


def delete(name: str) -> bool:
    if not name:
        return False
    qry = "delete from explorer where name=:name"
    params = {'name': name}
    curs.execute(qry, params)

    if curs.rowcount != 1:
        raise Missing(msg=f'Explorer {name} not found')

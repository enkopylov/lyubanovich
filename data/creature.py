from data.init import curs
from errors import Missing, Duplicate
from model.creature import Creature

curs.execute("""create table if not exists creature(
                name text primary key,
                description text,
                country text,
                area text)""")


def row_to_model(row: tuple):
    (name, description, country, area) = row
    return Creature(name=name, country=country, description=description, area=area)


def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()


def get_one(name: str) -> Creature:
    qry = "select * from creature where name=:name"
    params = {'name': name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f'Creature {name} not found')


def get_all() -> list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


def create(creature: Creature) -> Creature:
    qry = "insert into creature values (:name, :description, :country, :area)"
    params = model_to_dict(creature)
    try:
        curs.execute(qry, params)
    except:
        raise Duplicate(msg=f'Creature {creature.name} already exist')
    return get_one(creature.name)


def modify(creature: Creature) -> Creature:
    qry = ('''update creature 
                set country=:country,
                    name=:name,
                    description=:description,
                    area=:area
                where name= :name_orig''')
    params = model_to_dict(creature)
    params['name_orig'] = creature.name
    _ = curs.execute(qry, params)
    return get_one(creature.name)


def replace(creature: Creature):
    return creature


def delete(name: str) -> bool:
    if not name:
        return False
    qry = "delete from creature where name=:name"
    params = {'name': name}
    curs.execute(qry, params)

    if curs.rowcount != 1:
        raise Missing(msg=f'Creature {name} not found')

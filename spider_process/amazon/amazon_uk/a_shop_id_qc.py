from tools.tools_s.sql_base import get_data


def amazon_uk_shopid():
    table = input("表:")
    sql = '''select shop_id
    from {}'''.format(table)
    sql_prame = {
        "host": "192.168.0.227",
        "db": "ec_cross_brder",
        "port":9227,
        "user": "read",
        "password": "nriat227read@x#"
    }
    data = get_data(sql_prame,sql)

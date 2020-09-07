import pymysql


def main():
    conn = pymysql.connect(host='120.77.222.217', port=3306,
                           user='root', password='123123',
                           db='hrs', charset='utf8')
    try:
        with conn.cursor() as cursor:
            result = cursor.execute(
                'insert into tb_dept values (90,'销售二部',‘重庆’)')
            if result == 1:
                print('添加成功')
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    main()

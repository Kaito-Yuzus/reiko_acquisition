from sql_parsing import parser


def main(): 
    web_data = ['autofill', 'keywords']

    for table in web_data:
        db1 = parser.basic_db_parser('Web Data', table)
        db1.exporting_table()


if __name__ == '__main__':
    main()
from django.db import connection


def insert_qanda(question, answer):
    try:
        with connection.cursor() as cursor:  # withでcloseまでしてくれる
            sql1 = "INSERT INTO faq_qanda VALUES (nextval('faq_qanda_id_seq'),\'" + question + "\',\'" + answer + "\');"
            sql2 = "SELECT currval('faq_qanda_id_seq');"
            cursor.execute(sql1)
            cursor.execute(sql2)
            qandaid = cursor.fetchone()[0]  # リストの形で返ってきて最初の値がQandAid
        return qandaid
    except Exception:
        print("insert_qandaに失敗")
        if sql1 is not None:
            print("SQL1:" + sql1)
        if sql2 is not None:
            print("SQL2:" + sql2)
        raise Exception


def insert_index(qandaid, filtered_tokens):
    try:
        with connection.cursor() as cursor:
            for token_key, token_value in filtered_tokens.items():
                sql = "INSERT INTO faq_index VALUES (nextval('faq_index_id_seq'),\'" + token_key + "\'," + qandaid + "," + str(token_value) + ");"
                cursor.execute(sql)
    except Exception:
        print("insert_indexに失敗：" + sql)
        if sql is not None:
            print("SQL:" + sql)
        raise Exception


def update_qanda(qandaid, question, answer):
    try:
        with connection.cursor() as cursor:
            sql1 = "DELETE FROM faq_index WHERE qandaid = " + qandaid + ";"
            sql2 = "DELETE FROM faq_qanda WHERE id = " + qandaid + ";"
            sql3 = "INSERT INTO faq_qanda VALUES (" + qandaid + ",\'" + question + "\',\'" + answer + "\');"
            cursor.execute(sql1)
            cursor.execute(sql2)
            cursor.execute(sql3)
    except Exception:
        print("update_qandaに失敗")
        if sql1 is not None:
            print("SQL1:" + sql1)
        if sql2 is not None:
            print("SQL2:" + sql2)
        if sql3 is not None:
            print("SQL3:" + sql3)
        raise Exception


def search_qanda(word):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, question, answer FROM faq_qanda WHERE id IN (SELECT qandaid FROM faq_index WHERE token = \'" + word + "\' ORDER BY count);"
            cursor.execute(sql)
            searched_list = cursor.fetchall()
        return searched_list
    except Exception:
        print("search_qandaに失敗")
        if sql is not None:
            print("SQL:" + sql)
        raise Exception


def search_qanda2(splited_words):
    try:
        searched_lists = []
        with connection.cursor() as cursor:
            for word in splited_words:
                sql = "SELECT id, question, answer FROM faq_qanda WHERE id IN (SELECT qandaid FROM faq_index WHERE token = \'" + word + "\' ORDER BY count);"
                cursor.execute(sql)
                searched_lists = cursor.fetchall()
                searched_lists += searched_lists
            searched_lists = sorted([x for x in set(searched_lists) if searched_lists.count(x) > 1], key=searched_lists.index)  # 重複している項目のみ取り出す
        return searched_lists
    except Exception:
        print("search_qanda2に失敗")
        if sql is not None:
            print("SQL:" + sql)
        raise Exception


def delete_qa_and_index(qandaid):
    try:
        with connection.cursor() as cursor:
            sql1 = "DELETE FROM faq_qanda WHERE id = " + qandaid + ";"
            sql2 = "DELETE FROM faq_index WHERE qandaid = " + qandaid + ";"
            cursor.execute(sql1)
            cursor.execute(sql2)
    except Exception:
        print("delete_qa_and_indexに失敗")
        if sql1 is not None:
            print("SQL1:" + sql1)
        if sql2 is not None:
            print("SQL2:" + sql2)
        raise Exception


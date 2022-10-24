from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable
import random
class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

#NODE CREATION
    def create_node(self, word, lang):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_node, word, lang)
            for row in result:
                print("Created node: {word}".format(word=row['w']))

    @staticmethod
    def _create_node(tx, word, lang):
        query = ("CREATE (w:word{name:$word, lang:$lang}) "
            "RETURN w")
        result = tx.run(query, word=word, lang=lang)
        try:
            return [{"w": row["w"]["name"]}
                    for row in result]
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(query=query, exception=exception))
            raise

#RETURNING TRANSLATION OF TULU WORD
    def translate_tulu(self, tuluW):
        with self.driver.session() as session:
            result = session.read_transaction(self._translate_tulu, tuluW)
            for row in result:
                print("The translation of "+tuluW+ " is {w1} if the word type is {w2}.".format(w1=row['word'], w2=row['type']))
            return [(row['word'], row['type']) for row in result]

    @staticmethod
    def _translate_tulu(tx, tuluW):
        query = ("MATCH (b)-[r:TL]->(a) "
                "WHERE b.name = $tuluW "
                "RETURN a.name AS word, r.type AS type")
        result = tx.run(query, tuluW=tuluW)
        return [{"word": row["word"], "type": row["type"]} for row in result]

#RETURNING TRANSLATION OF ENGLISH WORD
    def translate_english(self, engW, type):
        with self.driver.session() as session:
            result = session.read_transaction(self._translate_engW, engW, type)
            for row in result:
                print("The translation of "+engW+ " is {a}.".format(a=row['word']))
            return [row['word'] for row in result]

    @staticmethod
    def _translate_engW(tx, engW, type):
        query = ("MATCH (b)-[r:TL]->(a) "
                "WHERE a.name = $engW AND r.type = $type "
                "RETURN b.name AS word")
        result = tx.run(query, engW=engW, type=type)
        return [{"word": row["word"]} for row in result]

#CONNECTION CREATION
    def create_link(self, engW, tuluW, type, gender):
        print("Creating link")
        with self.driver.session() as session:
            result = session.write_transaction(self._create_link, engW, tuluW, type, gender)
            for row in result:
                print("Created link between: {w1}, {w2}".format(w1=row['a'], w2=row['b']))

    @staticmethod
    def _create_link(tx, engW, tuluW, type, gender):
        print("Creating link part 2")
        query = ("MATCH (a:word), (b:word) "
            "WHERE a.name = $engW AND b.name = $tuluW "
            "CREATE (a)-[r:TL {type:$type, gender:$gender}]->(b) "
            "RETURN a, b")
        result = tx.run(query, engW=engW, tuluW=tuluW, type=type, gender = gender)
        try:
            return [{"a": row["a"]["name"], "b": row["b"]["name"]} for row in result]
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise

#FINDING NODE
    def find_word(self, word):
        print("Finding node")
        with self.driver.session() as session:
            result = session.read_transaction(self._find_and_return_word, word)
            for row in result:
                print("Found word: {row}".format(row=row))
                return row
            return 0


    @staticmethod
    def _find_and_return_word(tx, word):
        print("Finding node part 2")
        query = (
            "MATCH (w:word) "
            "WHERE w.name = $word "
            "RETURN w.name AS name"
        )
        result = tx.run(query, word=word)
        return [row["name"] for row in result]

#CHECKING CONNECTION BETWEEN TWO NODES

    def find_link(self, eng, tulu):
        print("Finding link")
        with self.driver.session() as session:
            result = session.read_transaction(self._find_and_return_link, eng, tulu)
            for row in result:
                print("Found connection: {row}".format(row=row))
                return row
            return 0

    @staticmethod
    def _find_and_return_link(tx, eng, tulu):
        print("Finding link part 2")
        query = (
            "MATCH (e:word)-[r:TL]->(t:word) "
            "WHERE e.name = $eng and t.name= $tulu "
            "RETURN r.type AS type"
            )
        #return TL word type instead of exists
        result = tx.run(query, eng=eng, tulu=tulu)
        return [row["type"] for row in result]

#FINDING ONE INSTANCE OF A WORD TYPE

    def find_same_type(self, type):
        with self.driver.session() as session:
            result = session.read_transaction(self._find_and_return_same_type, type)
            for row in result:
                print("Found word: {row}".format(row=row))
            w = [row for row in result]
        return w[0]

    @staticmethod
    def _find_and_return_same_type(tx, type):
        query = (
            "MATCH (e:word)-[r:TL]->(t:word) "
            "WHERE r.type = $type "
            "RETURN t.name AS name, rand() as ran "
            "ORDER BY ran "
            "LIMIT 1"
        )
        result = tx.run(query, type=type)
        return [row["name"] for row in result]

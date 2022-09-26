from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable

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


#CONNECTION CREATION
    def create_link(self, engW, tuluW, type):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_link, engW, tuluW, type)
            for row in result:
                print("Created link between: {w1}, {w2}".format(w1=row['a'], w2=row['b']))

    @staticmethod
    def _create_link(tx, engW, tuluW, type):
        query = ("MATCH (a:word), (b:word) "
            "WHERE a.name = $engW AND b.name = $tuluW "
            "CREATE (a)-[r:TL {type:$type}]->(b) "
            "RETURN a, b")
        result = tx.run(query, engW=engW, tuluW=tuluW, type=type)
        try:
            return [{"a": row["a"]["name"], "b": row["b"]["name"]} for row in result]
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise

#FINDING NODE
    def find_word(self, word):
        with self.driver.session() as session:
            result = session.read_transaction(self._find_and_return_word, word)
            for row in result:
                print("Found word: {row}".format(row=row))
                return 1
            return 0


    @staticmethod
    def _find_and_return_word(tx, word):
        query = (
            "MATCH (w:word) "
            "WHERE w.name = $word "
            "RETURN w.name AS name"
        )
        result = tx.run(query, word=word)
        return [row["name"] for row in result]

#CHECKING CONNECTION BETWEEN TWO NODES

    def find_link(self, eng, tulu):
        with self.driver.session() as session:
            result = session.read_transaction(self._find_and_return_link, eng, tulu)
            for row in result:
                print("Found connection: {row}".format(row=row))
                return row

    @staticmethod
    def _find_and_return_link(tx, eng, tulu):
        query = (
            "MATCH (e:word), (t:word) "
            "WHERE e.name = $eng and t.name= $tulu "
            "RETURN exists((e)-[:TL]->(t)) AS translation"
        )
        result = tx.run(query, eng=eng, tulu=tulu)
        return [row["translation"] for row in result]

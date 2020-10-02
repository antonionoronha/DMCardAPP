
from DMCard.models.solicitation import Solicitation
from DMCard.db import db
import random

class SolicitationBus(object):

    def add(self, client, address, income):
        score = random.randint(1,999)
        if score <= 299:
            status = "Reprovado"
            credit = 0
        elif score > 299 and score <= 599:
            status = "Aprovado"
            credit = 1000
        elif score > 599 and score <= 799:
            status = "Aprovado"
            if income >= 2000:
                credit = income * 0.5
            else:
                credit = 1000
        elif score > 799 and score <= 950:
            status = "Aprovado"
            credit = income * 2
        elif score > 950:
            status = "Aprovado"
            credit = 1000000

        solicitation = Solicitation(client=client, address=address, income=income, status=status, credit=credit, score=score)
        db.session.add(solicitation)
        db.session.commit()
        return solicitation

    def get_all(self):
        return Solicitation.query.all()

    def get_by_id(self, id):
        return Solicitation.query.filter(Solicitation.id == id).one()

    def delete_by_id(self, id):
        solicitation = Solicitation.query.filter(Solicitation.id == id).one()
        db.session.delete(solicitation)
        db.session.commit()
        return solicitation

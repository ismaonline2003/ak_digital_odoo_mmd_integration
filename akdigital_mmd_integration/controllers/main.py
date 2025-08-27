# -*- coding: utf-8 -*-
from odoo.http import Controller, request, route

class AkDigitalController(Controller):

    def create_reposition_body_validations(self, data):
        dict_return = {"status": "success", "message": "", "data": {}}



        return dict_return

    @route('/replacement', type='http', auth='none', methods=['POST'])
    def create_reposition(self, **kw):
        body_example = {
            "contract_number": "1234567",
            "contact": {
                "id": 1,
                "type": "person",#person, company
                "fullname": "Juan Garcia",
                "nif": "J-123456789-1",
                "phone": "1234567",
                "mobile": "123455678",
                "address": "Calle 1",
                "email": "example@gmail.com",
                "country_code": "NI",
                "province": {
                    "id": 1,
                    "name": "Provincia 1"
                },
                "city": {
                    "id": 1,
                    "name": "Ciudad 1"
                },
                "tags": [
                    {
                        "id": 1,
                        "name": "Tag 1"
                    }
                ]
            },
            "date": "2025-08-25",
            "warehouse_id": 1,
            "lines": [
                {
                    "product": {
                        "id": 1,
                        "cost": 5.00,
                        "price": 10.00,
                        "category_id": 1,
                        "ref": "A1",
                        "barcode": "AO93791",
                        "unit_of_measure": {
                            "id": 1,
                            "quantity": 1,
                            "name": "Unidad"
                        },
                        "weight": 1000
                    },
                    "price_unit": 10.00,
                    "quantity": 1.00
                }
            ]
        }

        body_validations = self.create_reposition_body_validations(kw)
        if body_validations.get("status", "") != "success":
            return {}#retornar codigo http




        print("create_reposition")
# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api, exceptions

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    _sql_constraints = [
        ('mmd_contract_number_uniq', 'unique(mmd_contract_number)', 'El Número de contrato de MMD debe ser único')
    ]

    mmd_contract_number = fields.Char(string="MMD Pawn - Contrato")

    def mmd_create_reposition_contact_body_validations(self, data):
        dict_return = {"status": "success", "message": "", "data": {}}

        if 'id' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contact > id'."
            })
            return dict_return

        if type(data['id']) != int:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'contact > id' must be an integer."
            })
            return dict_return

        if data['id'] == 0:
            dict_return.update({
                "status": "required_field",
                "message": "The field 'contact > id' is required."
            })
            return dict_return

        if 'type' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contact > type'."
            })
            return dict_return

        if type(data['type']) != str:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'contact > type' must be an string."
            })
            return dict_return

        if data['type'] not in ["company", "person"]:
            dict_return.update({
                "status": "invalid_value",
                "message": "The field 'contact > type' must have one of these values ('company', 'person')."
            })
            return dict_return

        if 'fullname' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contact > fullname'."
            })
            return dict_return

        if type(data['fullname']) != str:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'contact > fullname' must be a string."
            })
            return dict_return

        if not data['fullname']:
            dict_return.update({
                "status": "required_field",
                "message": "The field 'contact > fullname' is required."
            })
            return dict_return

        if 'nif' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contact > nif'."
            })
            return dict_return

        if type(data['nif']) != str:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'contact > nif' must be a string."
            })
            return dict_return

        nif = data['nif'].replace(" ", "")

        if not nif:
            dict_return.update({
                "status": "required_field",
                "message": "The field 'contact > nif' is required."
            })
            return dict_return

        if 'phone' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contact > phone'."
            })
            return dict_return

        if type(data['phone']) != str:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'contact > phone' must be a string."
            })
            return dict_return

        phone = data['phone'].replace(" ", "")

        if not phone:
            dict_return.update({
                "status": "required_field",
                "message": "The field 'contact > phone' is required."
            })
            return dict_return

        if 'mobile' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contact > mobile'."
            })
            return dict_return

        if type(data['mobile']) != str:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'contact > mobile' must be a string."
            })
            return dict_return

        mobile = data['mobile'].replace(" ", "")

        if not mobile:
            dict_return.update({
                "status": "required_field",
                "message": "The field 'contact > mobile' is required."
            })
            return dict_return

        if 'address' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contact > address'."
            })
            return dict_return

        if 'email' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contact > email'."
            })
            return dict_return

        if type(data['email']) != str:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'contact > email' must be a string."
            })
            return dict_return

        email = data['email'].replace(" ", "")

        if not email:
            dict_return.update({
                "status": "required_field",
                "message": "The field 'contact > email' is required."
            })
            return dict_return

        if 'country_code' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contact > country_code'."
            })
            return dict_return

        if type(data['country_code']) != str:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'contact > country_code' must be a string."
            })
            return dict_return

        country_code = data['country_code'].replace(" ", "")

        if not country_code:
            dict_return.update({
                "status": "required_field",
                "message": "The field 'contact > country_code' is required."
            })
            return dict_return

        if 'province_id' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contact > province_id'."
            })
            return dict_return

        if type(data['province_id']) != int:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'contact > province_id' must be an integer."
            })
            return dict_return

        if 'city_id' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contact > city_id'."
            })
            return dict_return

        if type(data['city_id']) != int:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'contact > city_id' must be an integer."
            })
            return dict_return

        if 'tags' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contact > tags'."
            })
            return dict_return

        if type(data['tags']) != list:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'contact > tags' must be a list."
            })
            return dict_return

        for tag in data['tags']:
            if 'id' not in tag:
                dict_return.update({
                    "status": "missing_field",
                    "message": "The field 'contact > tags > id' is required."
                })
                return dict_return

            if type(tag["id"]) != int:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'contact > tags > id' must be an integer."
                })
                return dict_return

            if tag["id"] == 0:
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'contact > tags > id' is required."
                })
                return dict_return

            if 'name' not in tag:
                dict_return.update({
                    "status": "missing_field",
                    "message": "The field 'contact > tags > ma,e' is required."
                })
                return dict_return

            if type(tag["name"]) != str:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'contact > tags > name' must be a string."
                })
                return dict_return

            tag_name = tag["name"].replace(" ", "")

            if not tag_name:
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'contact > tags > name' is required."
                })
                return dict_return

        return dict_return

    def mmd_create_reposition_lines_body_validations(self, lines):
        dict_return = {"status": "success", "message": "", "data": {}}

        for line in lines:

            if 'description' not in line:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > description'."
                })
                return dict_return

            if type(line['description']) != str:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > description' must be a string."
                })
                return dict_return

            if not line["description"].replace(" ", ""):
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'lines > description' is required."
                })
                return dict_return

            if 'product' not in line:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product'."
                })
                return dict_return

            if type(line['product']) != dict:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product' must be an object."
                })
                return dict_return

            if line["product"] == {}:
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'lines > product' is required."
                })
                return dict_return

            if 'id' not in line["product"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > id'."
                })
                return dict_return

            if type(line['product']['id']) != int:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > id' must be an integer."
                })
                return dict_return

            if line['product']['id'] == 0:
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'lines > product > id' is required."
                })
                return dict_return

            if 'name' not in line["product"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > name'."
                })
                return dict_return

            if type(line['product']['name']) != str:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > name' must be a string."
                })
                return dict_return

            if line['product']['name'].replace(" ", "") == "":
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'lines > product > name' is required."
                })
                return dict_return

            if 'cost' not in line["product"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > cost'."
                })
                return dict_return

            if type(line['product']['cost']) != float:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > cost' must be a float."
                })
                return dict_return

            if 'price' not in line["product"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > price'."
                })
                return dict_return

            if type(line['product']['price']) != float:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > price' must be a float."
                })
                return dict_return

            if 'category' not in line["product"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > category'."
                })
                return dict_return

            if type(line['product']['category']) != dict:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > category' must be an object."
                })
                return dict_return

            if line['product']['category'] == {}:
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'lines > product > category' is required."
                })
                return dict_return

            if 'id' not in line["product"]["category"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > category > id'."
                })
                return dict_return

            if type(line["product"]["category"]["id"]) != int:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > category > id' must be an integer."
                })
                return dict_return

            if line['product']['category']["id"] == 0:
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'lines > product > category > id' is required."
                })
                return dict_return

            if 'name' not in line["product"]["category"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > category > name'."
                })
                return dict_return

            if type(line["product"]["category"]["name"]) != str:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > category > name' must be a string."
                })
                return dict_return

            if line['product']['category']["name"].replace(" ", "") == "":
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'lines > product > category > name' is required."
                })
                return dict_return

            if 'ref' not in line["product"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > ref'."
                })
                return dict_return

            if type(line['product']['ref']) != str:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > ref' must be a string."
                })
                return dict_return

            if line['product']['ref'].replace(" ", "") == "":
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'lines > product > ref' is required."
                })
                return dict_return

            if 'barcode' not in line["product"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > barcode'."
                })
                return dict_return

            if type(line['product']['barcode']) != str:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > barcode' must be a string."
                })
                return dict_return

            if line['product']['barcode'].replace(" ", "") == "":
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'lines > product > barcode' is required."
                })
                return dict_return

            if 'unit_of_measure' not in line["product"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > unit_of_measure'."
                })
                return dict_return

            if type(line['product']['unit_of_measure']) != dict:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > unit_of_measure' must be a dict."
                })
                return dict_return

            if line['product']['unit_of_measure'] == {}:
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'lines > product > unit_of_measure' is required."
                })
                return dict_return

            if 'id' not in line["product"]["unit_of_measure"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > unit_of_measure > id'."
                })
                return dict_return

            if type(line["product"]["unit_of_measure"]["id"]) != int:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > unit_of_measure > id' must be an integer."
                })
                return dict_return

            if line["product"]["unit_of_measure"]["id"] == 0:
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'lines > product > unit_of_measure > id' is required."
                })
                return dict_return

            if 'quantity' not in line["product"]["unit_of_measure"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > unit_of_measure > quantity'."
                })
                return dict_return

            if type(line["product"]["unit_of_measure"]["quantity"]) != float:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > unit_of_measure > quantity' must be an float."
                })
                return dict_return

            if line["product"]["unit_of_measure"]["quantity"] == 0:
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'lines > product > unit_of_measure > quantity' is required."
                })
                return dict_return

            if 'name' not in line["product"]["unit_of_measure"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > unit_of_measure > name'."
                })
                return dict_return

            if type(line["product"]["unit_of_measure"]["name"]) != str:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > unit_of_measure > name' must be a string."
                })
                return dict_return

            if not line["product"]["unit_of_measure"]["name"].replace(" ", ""):
                dict_return.update({
                    "status": "required_field",
                    "message": "The field 'lines > product > unit_of_measure > name' is required."
                })
                return dict_return

            if 'weight' not in line["product"]:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > product > weight'."
                })
                return dict_return

            if type(line['product']['weight']) != float:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > product > weight' must be a float."
                })
                return dict_return

            if 'price_unit' not in line:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > price_unit'."
                })
                return dict_return

            if type(line['price_unit']) != float:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > price_unit' must be a float."
                })
                return dict_return

            if 'quantity' not in line:
                dict_return.update({
                    "status": "missing_field",
                    "message": "You must send the field 'lines > quantity'."
                })
                return dict_return

            if type(line['quantity']) != float:
                dict_return.update({
                    "status": "invalid_type",
                    "message": "The field 'lines > quantity' must be a float."
                })
                return dict_return


        return dict_return

    def mmd_create_reposition_body_validations(self, data):
        dict_return = {"status": "success", "message": "", "data": {}}
        required_fields = ["contract_number", "contact", "date", "warehouse_id", "lines"]

        if 'contract_number' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contract_number'."
            })
            return dict_return

        if type(data['contract_number']) != str:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'contract_number' must be an string."
            })
            return dict_return

        contract_number = data['contract_number'].replace(" ", "")

        if not contract_number:
            dict_return.update({
                "status": "required_field",
                "message": "The field 'contract_number' is required."
            })
            return dict_return

        if 'contact' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'contact'."
            })
            return dict_return

        if type(data['contact']) != dict:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'contact' must be an object."
            })
            return dict_return

        if data['contact'] == {}:
            dict_return.update({
                "status": "required_field",
                "message": "The field 'contact' is required."
            })
            return dict_return
        else:
            contact_body_validations = self.mmd_create_reposition_contact_body_validations(data["contact"])
            if contact_body_validations.get("status", "") != "success":
                return contact_body_validations

        if 'date' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'date'."
            })
            return dict_return

        if type(data['date']) != str:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'date' must be an string."
            })
            return dict_return

        date = data['date'].replace(" ", "")

        if not date:
            dict_return.update({
                "status": "required_field",
                "message": "The field 'contact' is required."
            })
            return dict_return

        if 'warehouse_id' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'warehouse_id'."
            })
            return dict_return

        if type(data['warehouse_id']) != int:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'warehouse_id' must be an integer."
            })
            return dict_return

        if data['warehouse_id'] == 0:
            dict_return.update({
                "status": "required_field",
                "message": "The field 'warehouse_id' is required."
            })
            return dict_return

        if 'lines' not in data:
            dict_return.update({
                "status": "missing_field",
                "message": "You must send the field 'lines'."
            })
            return dict_return

        if type(data['lines']) != list:
            dict_return.update({
                "status": "invalid_type",
                "message": "The field 'lines' must be a list."
            })
            return dict_return

        if len(data['lines']) == 0:
            dict_return.update({
                "status": "required_field",
                "message": "The field 'lines' is required."
            })
            return dict_return

        lines_validations = self.mmd_create_reposition_lines_body_validations(data["lines"])
        if lines_validations.get("status", "") != "success":
            return lines_validations

        return dict_return

    def mmd_create_reposition_partner(self, data):
        dict_return = {"status": "success", "message": "", "data": {}}
        mmd_id = str(data["id"])
        country_id = self.env["res.country"].search([('code', '=', data["country_code"])], limit=1)
        state_id = self.env["res.country.state"].search([('mmd_id', '=', mmd_id)], limit=1)
        city_id = self.env["res.country.city"].search([('mmd_id', '=', mmd_id)], limit=1)

        if not country_id:
            dict_return = {"status": "country_not_found",
                           "message": "El país con el código '{}' no fue encontrado.".format(data["country_code"]),
                           "data": data
                           }
            return dict_return

        if not state_id:
            dict_return = {"status": "province_not_found",
                           "message": "La provincia con el MMD ID '{}' no fue encontrada.".format(data["province_id"]),
                           "data": data
                           }
            return dict_return

        if not city_id:
            dict_return = {"status": "city_not_found",
                           "message": "La ciudad con el MMD ID '{}' no fue encontrada.".format(data["city_id"]),
                           "data": data
                           }
            return dict_return

        partner_id = self.env["res.partner"].create({
            "mmd_id": mmd_id,
            "company_type": data["type"],
            "name": data["fullname"],
            "vat": data["nif"],
            "phone": data["phone"],
            "mobile": data["mobile"],
            "street": data["address"],
            "email": data["email"],
            "country_id": country_id.id,
            "state_id": state_id.id,
            "city_id": city_id.id
        })

        dict_return["data"]["record"] = partner_id

        return dict_return

    def mmd_create_reposition_prepare_order_lines(self, lines):
        dict_return = {"status": "success", "message": "", "data": []}
        error_message = ""

        i = 1
        for line in lines:
            mmd_id = str(line["product"]["id"])
            categ_id_mmd_id = str(line["product"]["category"]["id"])
            uom_mmd_id = str(line["product"]["unit_of_measure"]["id"])
            product_id = self.env["product.template"].search([('mmd_id', '=', mmd_id)], limit=1)
            categ_id = self.env["product.category"].search([('mmd_id', '=', categ_id_mmd_id)], limit=1)
            uom_id =  self.env["uom.uom"].search([('mmd_id', '=', uom_mmd_id)], limit=1)

            if not product_id:
                if not categ_id:
                    error_message += ("-Linea de Orden # {}: La categoría de producto '{}' con el "
                                      "MMD ID {} no fue encontrada en Odoo.\n").format(
                        i, line["product"]["category"]['name'], categ_id_mmd_id)
                    i += 1
                    continue

                if not uom_id:
                    error_message += ("-Linea de Orden # {}: La unidad de medida '{}' con el "
                                      "MMD ID {} no fue encontrada en Odoo.\n").format(
                        i, line["product"]["unit_of_measure"]['name'], uom_mmd_id)
                    i += 1
                    continue

                product_id = product_id.create({
                    "purchase_ok": True,
                    "mmd_id": mmd_id,
                    "name": line["product"]["name"],
                    "standard_price": line["product"]["cost"],
                    "list_price": line["product"]["price"],
                    "categ_id": categ_id.id,
                    "default_code": line["product"]["ref"],
                    "barcode": line["product"]["barcode"],
                    "uom_id": uom_id.id,
                    "weight": line["product"]["weight"]
                })

            dict_return["data"].append((0, 0, {
                "product_id": product_id.product_variant_id.id,
                "price_unit": line["price_unit"],
                "product_qty": line["quantity"]
            }))
            i += 1

        if error_message != "":
            dict_return.update({
                "status": "order_line_error",
                "message": error_message,
                "data": {}
            })

        return dict_return

    def mmd_create_reposition(self, data):
        self = self.sudo()
        dict_return = {"status": "success", "message": "", "data": {}}
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
                "province_id": 1,
                "city_id": 1,
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

        body_validations = self.mmd_create_reposition_body_validations(data)
        if body_validations.get("status", "") != "success":
            return body_validations

        order_id = self.env["purchase.order"].search([('mmd_contract_number', '=', data["contract_number"])], limit=1)

        if order_id:
            dict_return = {"status": "reposition_already_exists",
                           "message": "La reposición enviada ya esta registrada en Odoo.",
                           "data": data
                           }
            return dict_return

        partner_id = self.env["res.partner"].search([('mmd_id', '=', str(data["contact"]["id"]))], limit=1)

        if not partner_id:
            partner_id_creation = self.mmd_create_reposition_partner(data["contact"])

            if partner_id_creation.get("status", "") != "success":
                return partner_id_creation

            partner_id = partner_id_creation["data"]["record"]

        prepare_order_lines = self.mmd_create_reposition_prepare_order_lines(data["lines"])

        if prepare_order_lines["status"] != "success":
            return prepare_order_lines

        warehouse_mmd_id = str(data["warehouse_id"])
        warehouse_id = self.env["stock.warehouse"].search([('mmd_id', '=', warehouse_mmd_id)], limit=1)

        if not warehouse_id:
            dict_return = {"status": "warehouse_not_found",
                           "message": "El almacen con el MMD ID {} no fue encontrado.".format(warehouse_mmd_id),
                           "data": data
                           }
            return dict_return

        if not warehouse_id.reposition_type_id:
            dict_return = {"status": "reposition_type_not_established",
                           "message": "Se debe establecer un tipo de operación para "
                                      "reposiciones en al almacen con el MMD ID {} "
                                      "(En el sistema Odoo).".format(warehouse_mmd_id),
                           "data": data
                           }
            return dict_return

        try:
            date_order = datetime.datetime.strptime(data["date"], "%Y-%m-%d")
        except Exception as error:
            dict_return = {"status": "invalid_date",
                           "message": "La fecha es incorrecta.",
                           "data": data
                           }
            return dict_return

        date_order = date_order.date()

        record_data = {
            "mmd_contract_number": data["contract_number"],
            "partner_id": partner_id.id,
            "date_order": date_order,
            "order_line": prepare_order_lines["data"],
            "picking_type_id": warehouse_id.in_type_id.id
        }

        purchase_order_id = self.env["purchase.order"].create(record_data)
        purchase_order_id.button_confirm()
        purchase_order_id.picking_ids.button_validate()
        dict_return["data"] = purchase_order_id.id
        return dict_return
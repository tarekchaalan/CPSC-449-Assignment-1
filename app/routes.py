from flask_restx import Api, Namespace, Resource, fields, abort
from app import db
from app.models import InventoryItem
from sqlalchemy.exc import DataError, IntegrityError

api = Api()
ns = Namespace('inventory', description='Inventory Management API - CPSC 449 Assignment 1')

# Register namespaces
api.add_namespace(ns)

# Models for marshalling
inventory_item_model = api.model('InventoryItem', {
    'id': fields.Integer(readonly=True, description='The inventory unique identifier'),
    'name': fields.String(required=True, description='The name of the inventory item'),
    'quantity': fields.Integer(required=True, description='The quantity of the item'),
    'description': fields.String(description='The description of the item'),
    'unit_price': fields.Float(required=True, description='The unit price of the item'),
})

def get_payload_value(data, key, default=None, required=True):
    try:
        return data[key] if required else data.get(key, default)
    except KeyError:
        ns.abort(400, f"The '{key}' field is required in the request body.")

# Inventory Items Endpoints
@ns.route('/')
class InventoryList(Resource):
    @ns.marshal_list_with(inventory_item_model)
    def get(self):
        '''List all inventory items'''
        items = InventoryItem.query.all()
        return items

    @ns.expect(inventory_item_model)
    @ns.marshal_with(inventory_item_model, code=201)
    def post(self):
        '''Create a new inventory item'''
        data = api.payload
        name = get_payload_value(data, 'name')
        quantity = get_payload_value(data, 'quantity')
        description = get_payload_value(data, 'description', default='', required=False)
        unit_price = get_payload_value(data, 'unit_price')
        item = InventoryItem(name=name, quantity=quantity, description=description, unit_price=unit_price)
        db.session.add(item)
        db.session.commit()
        return item, 201

@ns.route('/<int:id>')
@ns.response(404, 'Inventory item not found')
@ns.param('id', 'The inventory item unique identifier')
class InventoryItemResource(Resource):
    @ns.marshal_with(inventory_item_model, envelope='data')
    def get(self, id):
        '''Fetch a single inventory item'''
        item = InventoryItem.query.get(id)
        if not item:
            ns.abort(404, f"Inventory item with ID {id} does not exist.")
        return item

    @ns.expect(inventory_item_model)
    def put(self, id):
        '''Update an existing inventory item'''
        item = InventoryItem.query.get_or_404(id)
        data = api.payload

        try:
            item.name = get_payload_value(data, 'name', item.name, required=False)
            item.quantity = get_payload_value(data, 'quantity', item.quantity, required=False)
            item.description = get_payload_value(data, 'description', item.description, required=False)
            item.unit_price = get_payload_value(data, 'unit_price', item.unit_price, required=False)

            db.session.commit()
        except DataError as e:
            db.session.rollback()
            # Example of extracting specific info from a DataError using f-string
            if 'quantity' in str(e.orig):
                message = f"Failed to update item with ID:{id} due to Quantity value being out of range."
            else:
                message = f"Failed to update item with ID:{id} due to Invalid input data."
            return {"message": message}, 400
        except IntegrityError:
            db.session.rollback()
            # Handle other integrity issues, such as foreign key constraints using f-string
            message = f"Failed to update item with ID:{id} due to a data integrity issue."
            return {"message": message}, 400

        return ns.marshal(item, inventory_item_model), 200

    @ns.response(200, 'Inventory item deleted successfully')
    def delete(self, id):
        '''Delete a single inventory item'''
        # Manually check for the item's existence
        item = InventoryItem.query.get(id)
        if not item:
            # Item not found, so we use abort to return a custom 404 message
            abort(404, f"ID:{id} could not be found and therefore not deleted.")

        db.session.delete(item)
        db.session.commit()
        return {"message": f"ID:{id} Deleted Successfully"}, 200

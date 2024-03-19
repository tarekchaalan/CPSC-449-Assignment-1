from flask_restx import Api, Namespace, Resource, fields
from app import db
from app.models import InventoryItem

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

# Inventory Items Endpoints
@ns.route('/inventory')
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
        item = InventoryItem(name=data['name'],
                             quantity=data['quantity'],
                             description=data.get('description', ''),
                             unit_price=data['unit_price'])
        db.session.add(item)
        db.session.commit()
        return item, 201

@ns.route('/inventory/<int:id>')
@ns.response(404, 'Inventory item not found')
@ns.param('id', 'The inventory item unique identifier')
class InventoryItemResource(Resource):
    @ns.marshal_with(inventory_item_model)
    def get(self, id):
        '''Fetch a single inventory item'''
        item = InventoryItem.query.get_or_404(id)
        return item

    @ns.expect(inventory_item_model)
    @ns.marshal_with(inventory_item_model)
    def put(self, id):
        '''Update an existing inventory item'''
        item = InventoryItem.query.get_or_404(id)
        data = api.payload
        item.name = data.get('name', item.name)
        item.quantity = data.get('quantity', item.quantity)
        item.description = data.get('description', item.description)
        item.unit_price = data.get('unit_price', item.unit_price)
        db.session.commit()
        return item

    @ns.response(200, 'Inventory item deleted successfully')
    def delete(self, id):
        '''Delete a single inventory item'''
        item = InventoryItem.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Deleted Successfully"}, 200

# Pizza-Delivery-API
A Pizza Delivery API project for a pizza delivery service.
|METHOD     | ROUTE     | FUNCTIONALITY            | ACCESS
| :------------ |   :---:       | --------:        |--------:
| POST        | /api/signup       | Register new user        |All users
| POST         | /api/login         | Login user    |All users
| POST         | /api/order         | Place an order    |All users
| PUT        | /api/order/update/{order_id}/       | Update an order        |All users
| PUT         | /api/order/status/{order_id}/        | Update order status    |Superuser
| DELETE        | /api/order/delete/{order_id}/      | Delete an order        |All users
| GET         | /api/user/orders/         | Get user's orders    |All users
| GET        | /api/orders/       | List all orders made        |Superuser
| GET        | /api/orders/{order_id}/        | Retrieve an order    |Superuser
| GET        | /api/user/order/{order_id}/         | Get user's specific order    |All users
| GET        | /docs/         | View API Documentations    |All users

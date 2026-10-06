from conduit.app import create_app
from conduit.settings import TestConfig
from conduit.database import db
app=create_app(TestConfig)
with app.app_context(): db.create_all()
print(app.url_map,flush=True)
app.run(host='127.0.0.1',port=3000,use_reloader=False)

import config
import views
from loader import app

views.setup()

app.run(debug=True, host='0.0.0.0', port=config.APP_PORT)

import views
from loader import app

views.setup()

app.run(debug=True, port=80)

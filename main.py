import vk_api
import json
from flask import Flask, request



vk_session = vk_api.VkApi(token=API_TOKEN)
api = vk_session.get_api()
app = Flask(__name__)


@app.route('/', methods=["POST"])
def handling_post():
  data = json.loads(request.data)
  if 'type' not in data.keys():
    return 'not vk request'
  if data['type'] == 'confirmation':
    return CONFIRMATION_TOKEN







if __name__ == '__main__':
  app.run()
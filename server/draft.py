# @blueprint.route('/test', methods=["GET"])
# def get_relation():
#   h = posts.aggregate([
#       {
#           "$lookup":
#           {
#               "from": "comments",
#               "localField": "_id",
#               "foreignField": "postId",
#               "as": "comments"
#           }
#       },
#       {"$match": {"_id": ObjectId("5b5945022f021105b4744ad4")}},
#       {"$project": {"_id": 0, "_create": 0, "user": 0,
#                     "username": 0, "comments.postId": 0, "comments._id": 0}}
#   ])
#   # h = posts.aggregate([
#   # {
#   #   "$lookup":
#   #      {
#   #        "from": "comments",
#   #        "let": { "id": "_id"},
#   #        "pipeline": [
#   #           { "$match": {"_id": ObjectId("5b5eb0292f02110f96a03752")}},
#   #           { "$project": { "postId": 0, "_id": 0} }
#   #        ],
#   #        "as": "comments"
#   #      }
#   # },
#   #      { "$match" : { "_id" : ObjectId("5b5945022f021105b4744ad4")}},
#   #      { "$project" : { "_id": 0, "_create": 0, "user": 0, "username": 0} }
#   # ])
#   return Utils.return_jsonify(list(h))
#   
class base:
  @classmethod
  def get_name(cls):
    return cls.__name__

class phu(base):
	def getlist(self):
		return phu.get_name()

print(phu().getlist())
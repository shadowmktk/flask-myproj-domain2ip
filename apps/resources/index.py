from flask import Blueprint, request, current_app
from flask_restful import Api, Resource
from ..services.index import get_domain_ip
        

indexbp = Blueprint("index", __name__)
api = Api(indexbp)


class IndexResource(Resource):
    def get(self):
        try:
            domain = request.args.get("domain", None)
            if domain:
                nameservers = request.args.get("nameservers", None)
                if nameservers:
                    result = get_domain_ip(domain, "A", [nameservers])
                else:
                    result = get_domain_ip(domain, "A")
                    
                return {f"域名": domain, f"DNS": [nameservers], "IP地址": [str(x) for x in result.rrset]}
            else:
                return {"error": f"缺少domain参数"}, 400
        except Exception as e:
            current_app.logger.error(e)
            return {"error": f"出错了 换个域名或DNS试试"}, 400

        
api.add_resource(IndexResource, '/')
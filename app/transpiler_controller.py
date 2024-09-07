import requests

class TranspilerController:
    def __init__(self):
        self.lang_frontend_endpoints = {
            "dart": "http://localhost:8080",
            "kotlin": "http://localhost:8081"
        }
    
    def transpile(self, input_code, source_lang, target_lang):
        ast_response, ast_errors = self.generate_ast(input_code, source_lang)

        if ast_errors:
            return (None, ast_errors)

        transpile_result  =  self.generate_code(ast_response, target_lang)
        
        return transpile_result


    def generate_ast(self, input_code, source_lang):
        endpoint_to_query = self.lang_frontend_endpoints[source_lang] + "/generate-ast"

        r = requests.post(endpoint_to_query, json={'code': input_code})
        response_dict = r.json()
        
        success = response_dict["success"]

        if success:
            response_dict.pop("success", None)
            response_dict.pop("errors", None)
            return(response_dict, None)
        else:
            errors = response_dict["errors"]
            errors = errors[0]
            errors_message = errors["message"]
            errors_position = errors["position"]
            errors = "Error! "+ str(errors_message) + ", try check " + str(errors_position)
            return(None, errors)
        
    def generate_code(self, request, source_lang):
        endpoint_to_query = self.lang_frontend_endpoints[source_lang] + "/generate-code"

        g = requests.post(endpoint_to_query, json=request)

        transpile_result = g.json()
        output_code = transpile_result["code"]
        success = transpile_result["success"]

        if success:
            return (output_code, None)
        else:
            errors = response_dict["errors"]
            errors = errors[0]
            errors_message = errors["message"]
            errors_position = errors["position"]
            errors = "Error! " + str(errors_message) + ", try check " + str(errors_position)
            return (None, errors)

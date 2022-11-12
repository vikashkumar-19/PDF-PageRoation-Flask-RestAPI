from flask import Flask, request
from flask_restful import Resource, Api

import PyPDF2

app = Flask(__name__)
# create API object
api = Api(app)


class Hello(Resource):
    def get(self):
        return {"message":"Hello !!  You can use '/rotate?file_path=<string> & angle_of_rotation=<int> & page_number = <int>' to rotate a pdf's page"}



# Class to handle Rest calls
class PDF_rotate(Resource):
    
    def get(self):
        
        # Extracting parameters
        file_path = request.args.get("file_path")
        angle_of_rotation = int(request.args.get("angle_of_rotation"))
        page_number = int(request.args.get("page_number"))
        
        # angle of rotation filter to 0, 90, 180, 270 value
        angle_of_rotate_filter = (angle_of_rotation)%360
        pdfFileObj =  open(file_path,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pdfWriter = PyPDF2.PdfFileWriter()
        
        # Validating the given input
        if(page_number> pdfReader.numPages or page_number<=0):
            return {"error":"page_number is not valid"}
        elif(angle_of_rotation%90 !=0):
            return {"error":"angle_of_rotation is not valid! Should be multiple of 90"}
        
        # iteration through pdf and rotate specified page 
        for page in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(page)
            if((page+1) == page_number):
                pageObj.rotateClockwise(angle_of_rotate_filter)
            pdfWriter.addPage(pageObj)
        
        # Trim beginning and ending whitespaces
        file_path = file_path.strip()
        
        # New File name with nomenclature of Roation angle and page number
        new_file_path = file_path[:-4]+"_new_"+str(angle_of_rotation)+"_rotated_file_at_page_number_"+str(page_number)+".pdf"

        # Exporting new file
        newFile =  open(new_file_path,"wb")
        pdfWriter.write(newFile)
        pdfFileObj.close()
        newFile.close()


        # Return Response 
        return {
            "new_file_path": new_file_path,
            "old_file":file_path,
            "angle_of_rotation":angle_of_rotation,
            "page_number":page_number
            }






 
api.add_resource(Hello,"/")
api.add_resource(PDF_rotate,'/rotate')


if __name__ == '__main__':
    app.run(debug=True)

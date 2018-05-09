const nano = require('nano')('http://localhost:5984');
var response;
function initialConnection(dbname){

    nano.db.get(dbname, function(err, body) {
            if (!err) {
                response=body
                console.log(response);
            }
        });
}



function dbConnection(dbname) {
    initialConnection(dbname)
//    console.log(dbrespons);
//    return JSON.stringify(response);
    return response
    
}
//dbConnection.push(dbname)
module.exports = dbConnection
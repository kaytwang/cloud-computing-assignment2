const router = require('koa-router')()
const dbConnection = require('../dbConnection.js');
var PassThrough = require('stream').PassThrough;
var fs = require('fs')
var res
var readLine = require('lei-stream').readLine;
var onetwo;
var three;

router.get('/', async (ctx, next) => {
    onetwo = reader('504target.json');
    three = reader('employ2006.json');
//    console.log(dataResponse)
    await ctx.render('index.html', {})
})

router.get('/onetwo', async (ctx, next) => {
    var call = 0
    ctx.response.type='application/json';'charset=utf-8';
//    ctx.response.set('Cache-Control', 'no-cache');
    ctx.response.set({'Access-Control-Allow-Origin':'*',
                      'Content-Type':'text/event-stream',
                      'Cache-Control':'no-cache'
                     });

    var date = ""
    data = JSON.stringify(onetwo[call])
    let r = `retry: 10000\ndata:${date}\n\n`
    const stream = new PassThrough()
    var interval = setInterval(function(){
        date =  JSON.stringify(onetwo[call])
        r = `retry: 10000\ndata:${date}\n\n`
        stream.write(r)
        call++
        if(call==10000){
//            stream
            clearInterval(interval)
        }
    }, 6)
    
    ctx.response.body = stream
})

router.get('/three', async (ctx, next) => {
     var call = 0
    ctx.response.type='application/json';'charset=utf-8';
//    ctx.response.set('Cache-Control', 'no-cache');
    ctx.response.set({'Access-Control-Allow-Origin':'*',
                      'Content-Type':'text/event-stream',
                      'Cache-Control':'no-cache'
                     });

    var date = ""
    data = JSON.stringify(three[call])
    let r = `retry: 10000\ndata:${date}\n\n`
    const stream = new PassThrough()
    var interval = setInterval(function(){
        date =  JSON.stringify(three[call])
        r = `retry: 10000\ndata:${date}\n\n`
        stream.write(r)
        call++
        if(call==three.length){
            clearInterval(interval)
        }
    }, 1)
//    if(call!=three.length){
        ctx.response.body = stream
//    }
})


function reader(file){
  
    var dataResponse = new Array();
    var pathhead = './public/javascripts/'
    var s = readLine(fs.createReadStream(pathhead+file), {
      
      newline: '\n',
     
      autoNext: false,
      
      encoding: function (data) {
//          console.log("hello")
          dataResponse.push(JSON.parse(data))
        return JSON.parse(data);
      }
    });
    
    s.on('data', function (data) {
//      console.log(data);
      s.next();
    });
    
    s.on('end', function () {
//        console.log(dataResponse)
        console.log('end');
    });
    
    return dataResponse
}

module.exports = router

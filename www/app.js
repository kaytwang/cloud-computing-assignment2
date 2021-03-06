const Koa = require('koa')
const app = new Koa()
const views = require('koa-views')
const json = require('koa-json')
const onerror = require('koa-onerror')
const bodyparser = require('koa-bodyparser')
const logger = require('koa-logger')
const templating = require('./templating');
const bodyParser = require('koa-bodyparser');

const index = require('./routes/index')
const users = require('./routes/users')
const isProduction = process.env.NODE_ENV === 'production';

app.use(templating('views', {
    noCache: !isProduction,
    watch: !isProduction
}));

// error handler
onerror(app)

// middlewares
app.use(bodyparser({
  enableTypes:['json', 'form', 'text']
}))
app.use(json())
app.use(logger())
app.use(require('koa-static')(__dirname + '/public'))

app.use(views(__dirname + '/views', {
  extension: 'html'
}))



// logger
app.use(async (ctx, next) => {
  const start = new Date()
  await next()
  const ms = new Date() - start
  console.log(`${ctx.method} ${ctx.url} - ${ms}ms`)
})


// routes
//app.use(controller());
app.use(index.routes(), index.allowedMethods())
app.use(users.routes(), users.allowedMethods())
if (! isProduction) {
    let staticFiles = require('./static-files');
    app.use(staticFiles('/public/', __dirname + '/public'));
    let viewFiles = require('./static-files');
    app.use(staticFiles('/views/', __dirname + '/views'));
}

app.use(templating('views', {
    noCache: !isProduction,
    watch: !isProduction
}));

//database
//let dbConnection = require('./dbConnection');
////console.log(typeof(dbConnection('test')));
//app.use(dbConnection('test'));


// error-handling
app.on('error', (err, ctx) => {
  console.error('server error', err, ctx)
});

module.exports = app

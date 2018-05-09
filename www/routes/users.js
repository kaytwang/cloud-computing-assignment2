const router = require('koa-router')()
const dbConnection = require('../dbConnection.js');

router.prefix('/users')

router.get('/', function (ctx, next) {
    re = dbConnection('test')
   ctx.body = re
})

router.get('/bar', function (ctx, next) {
  ctx.body = 'this is a users/bar response'
})

module.exports = router

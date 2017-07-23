var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


router.get('/search', function(req, res, next) {
  console.log(req.query.q);
	res.render('search_res', 
	        { title: 'Search Resuslts for '+ req.query.q
	        });

});


module.exports = router;

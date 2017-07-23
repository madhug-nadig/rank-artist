var express = require('express');
var router = express.Router();

var caches = require('../models/caches');


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


router.get('/search', function(req, res, next) {
  console.log(req.query.q);
  /*data = [{
          "final_score": 29.001,
          "topic_score": 0.0,
          "link": "https://www.nerdwallet.com/blog/loans/cost-tesla/",
          "title": "Tesla Cars: 2017 Tesla Prices, Reviews, Specs",
          "lang_score":90.5,
          "content": "Tesla's luxurious, all-electric speedsters have everyone's head turned. But before you trade your kid's college fund for one, let's evaluate how much it will actually cost you.",
          "luhn_score":28,
          "text_score":30
        }]
        */

  caches.find({}, function(err, data){
  	console.log(data);
  	if(err){
  		console.log(err);
  	}
	res.render('search_res', 
	        { title: req.query.q,
	          results : JSON.stringify(data)
	        });
	});
});


module.exports = router;

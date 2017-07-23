var express = require('express');
var router = express.Router();

var caches = require('../models/caches');


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Rank Artist - By Neural Titanium' });
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

  caches.find({"query": req.query.q + '\n'}, function(err, data){
  	console.log(data);
  	if(err){
  		console.log(err);
  	}
  	if(data.length == 0){
  		d = ['http://138.197.29.147:3000/search?q=What+is+the+state+of+the+art+on+autonomous+cars+%3F', 'http://138.197.29.147:3000/search?q=what+is+the+best+ubisoft+game', 'http://138.197.29.147:3000/search?q=Which+are+the+best+games+of+2017+%3F', 'http://138.197.29.147:3000/search?q=what+is+the+review+on+assassin%27s+creed+%3F','http://138.197.29.147:3000/search?q=How+strategically+challenging+are+Ubisoft+games%3F', 'http://138.197.29.147:3000/search?q=How+much+is+the+price+of+a+tesla+', 'http://138.197.29.147:3000/search?q=Which+is+the+most+expensive+gaming+device+%3F', 'http://138.197.29.147:3000/search?q=Did+the+popularity+of+Assassin%27s+Creed+decrease+from+the+year+2016+to+2017+%3F']
  		res.redirect( d[(Math.floor(Math.random() * ((d.length-1) - 0 + 1)) + 0)]+ '&redirect=true')
  	}
  	else{
		res.render('search_res', 
		        { title: req.query.q,
		          results : JSON.stringify(data)
		        });
		}
	});

});

router.get('/cached', function(req, res, next) {
  res.render('cache', { title: 'Cached Results' });
});



module.exports = router;

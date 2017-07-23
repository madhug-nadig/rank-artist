var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var cacheSchema = new Schema({
    final_score: {
        type: Number,
        required: true
    },
    topic_score: {
        type: Number,
        required: true
    },
    link: {
        type: String,
        required: true
    },
    title:{
        type: String,
        required: false
    },
    lang_score: {
        type: Number,
        required: true
    },
    luhn_score: {
        type: Number,
        required: true
    },
    content: {
        type: String,
        required: true
    },
    text_score: {
        type: Number,
        required: true
    }
}, {
    timestamps: true
});


var caches = mongoose.model('caches', cacheSchema);

module.exports = caches;
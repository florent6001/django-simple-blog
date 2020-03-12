const purgecss = require('@fullhuman/postcss-purgecss')
const cssnano = require('cssnano')

module.exports = {
    plugins: [
        require('postcss-node-sass'),
        cssnano({
            preset: 'default'
        }),
        purgecss({
            content: ['./*/*/*.html', './*/*.html'],
            defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || []
        })
    ]
}
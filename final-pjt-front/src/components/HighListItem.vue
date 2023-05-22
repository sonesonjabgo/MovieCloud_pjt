<template>
    <img id='poster' :src="getPosterImage"> 
</template>

<script>

// const API_URL = 'http://127.0.0.1:8000'

export default {
    name : 'HighListItem',
    props: {
        highmovie : Object,
    },
    computed: {
        getPosterImage(){
        return `https://image.tmdb.org/t/p/w200${this.highmovie.poster_path}`
        }
    },
}
</script>

<style>

</style>
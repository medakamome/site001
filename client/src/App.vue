<template>
  <v-container fluid grid-list-md>
    <v-slide-y-transition mode="out-in">
      <v-layout row wrap align-center>
        <v-flex v-for="difinition in difinitionList">
          <v-card>
            <v-card-title>
              <span class="headline">{{ difinition.name }}</span>
            </v-card-title>
            <v-card-text>
              <blockquote>
                {{ difinition.difinition }}
                <footer>
                  <small>
                    <em>&mdash;{{ difinition.updated_at }}</em>
                  </small>
                </footer>
              </blockquote>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-slide-y-transition>
  </v-container>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import axios from 'axios'

export default {
  data () {
    return {
      difinitionList: []
    }
  },
  mounted: function () {
    console.log('mounted')
    // APIを叩く。
    // 開発サーバで動作中はちゃんとDjangoの8000番ポートを叩いてくれます。
    axios.get('api/difinitions/')
      .then((response) => {
        this.difinitionList = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>
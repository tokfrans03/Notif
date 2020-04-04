<template>
  <v-app>
    <v-text-field
      name="url"
      label="url"
      v-model="url"
    ></v-text-field>
    <v-form>
      <v-text-field
        name="Titel"
        label="Titel"
        v-model="Titel"
      ></v-text-field>
      <v-text-field
        name="message"
        label="message"
        v-model="message"
      ></v-text-field>
      <v-btn color="success" @click="send()">send</v-btn>
    </v-form>
    <v-alert type="primary" :value="response">
      {{response}}
    </v-alert>
  </v-app>
</template>

<script>
// @ is an alias to /src
const axios = require('axios');

export default {
  name: 'Home',
  data() {
    return {
      Titel: "",
      message: "",
      url: "localhost",
      response: ""

    }
  },
  methods: {
    send(){
      let data = {
        "title": this.title,
        "message": this.message
      }
      let self = this;
      axios.get(this.url + ":8000", data).then(function (response) {
        self.response = response.data
      })
    }
  },
}
</script>

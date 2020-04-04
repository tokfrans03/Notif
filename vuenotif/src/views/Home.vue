<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on }">
        <v-btn color="green" dark v-on="on">Skicka medelande</v-btn>
      </template>
      <v-form class="pa-4">
        <v-text-field name="url" label="url" v-model="url"></v-text-field>
        <v-text-field name="title" label="Titel" v-model="title"></v-text-field>
        <v-text-field name="message" label="Medelande" v-model="message"></v-text-field>
        <v-text-field name="img" label="Bild URL" v-model="img"></v-text-field>
        <v-btn color="success" :loading="loading" @click="send()">send</v-btn>
      </v-form>
      <v-alert :color="response_color" :value="Boolean(response)">{{response}}</v-alert>
    </v-dialog>
  </div>
</template>

<script>
// @ is an alias to /src
const axios = require("axios");

export default {
  name: "Home",
  data() {
    return {
      title: "",
      message: "",
      img: "",
      url: "http://localhost",
      response: "",
      response_color: "error",
      loading: false
    };
  },
  methods: {
    send() {
      let data = {
        title: this.title,
        message: this.message,
        imgurl: this.img
      };
      console.log(data);
      let self = this;
      this.loading = true;
      let url = this.url + ":8000";
      axios
        .post(url, data)
        .then(function(response) {
          self.response = response.data.value;
          self.response_color = response.data.Success ? "success" : "error";

          self.loading = false;
        })
        .catch(function(error) {
          // handle error
          self.response = error + "  ==  Is the server running?";
          self.response_color = "error";
          self.loading = false;
        });
    }
  }
};
</script>

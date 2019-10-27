<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Conversation Starters</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        text
        href="https://github.com/Robooto/conversation-starter"
        target="_blank"
      >
        <span class="mr-2">Github</span>
      </v-btn>
    </v-app-bar>

    <v-content>
      <Conversations/>
    </v-content>
  </v-app>
</template>

<script>
import Conversations from './components/Conversations';

export default {
  name: 'App',
  components: {
    Conversations,
  },
  data: () => ({
    //
  }),
};
</script>

<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >
      <v-flex mb-4 mt-4>
        <h1 class="display-2 font-weight-bold mb-3">
          Select a topic below to get a conversation starter!
        </h1>
      </v-flex>
      <v-flex
        mb-5
        xs12
      >
        <v-btn color="primary" @click="roulette" class="mb-4">Roulette</v-btn>


            <v-card
              class="mx-auto"
              max-width="600"
              min-height="75"
            >
              <v-list-item-title class="pt-6 pb-6">
                {{starter}}
              </v-list-item-title>
            </v-card>
      </v-flex>

      <v-flex
        xs12
        mb-5
      >
        <h2 class="headline font-weight-bold mb-3">Topics</h2>

        <v-layout justify-center>
          <a
            v-for="(topic, i) in topics"
            :key="i"
            class="subheading mx-3"
            @click="topicClick(topic)"
          >
            {{ topic }}
          </a>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { dataService } from '../shared'
export default {
  data: () => ({
    topics: [],
    starter: 'Click a topic or smash the roulette button!',
  }),
  async created() {
    await this.loadTopics();
  },
  methods: {
    async topicClick(topic) {
      this.starter = await dataService.getStarter(topic).catch(console.log);
    },
    async loadTopics() {
      this.topics = await dataService.getTopics().catch(console.log);
    },
    async roulette() {
      this.starter = await dataService.getRandom().catch(console.log);
    }
  }
};
</script>

<template>
    <div>
        RESULT LIST

        <div v-for="(choosable, index) in props.widget.choosables.sort((a,b) => a.rank - b.rank)" :key="index">
          <RankedChoosable :choosable="choosable"/>
        </div>
    </div>
</template>
<script setup lang="ts">
import type {ResultListWidget } from '~/sdk';
import RankedChoosable from './RankedChoosable.vue';


interface WidgetProps {
  widget: ResultListWidget;
}

const props = defineProps<WidgetProps>();

</script>
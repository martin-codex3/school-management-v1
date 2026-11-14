<script lang="ts">
    import type { PageProps } from "../$types";

    let { data }: PageProps = $props();
</script>

<div>
    <h1>This is the profile page</h1>
    <p>{data.user.first_name}</p>
</div>

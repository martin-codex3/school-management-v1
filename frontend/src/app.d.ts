// See https://svelte.dev/docs/kit/types#app.d.ts

import type { Token } from "#lib/types/token/toke.ts";

// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		interface Locals {
			token: Token
		}
		interface PageData { }
		// interface PageState {}
		// interface Platform {}
	}
}

export { };

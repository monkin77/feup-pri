import { stringToHash } from "../utils/utils";

export const itemStates = {
    todo: "TODO",
    done: "DONE"
};

export class Item {
    constructor(text, state) {
        this.text = text;
        this.state = state;
        this.id = stringToHash(this.text);
    }
}
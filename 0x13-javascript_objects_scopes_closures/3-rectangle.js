#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0) {
            // If width or height is not a positive integer, create an empty object
            this.width = null;
            this.height = null;
        } else {
            // Initialize instance attributes width and height
            this.width = w;
            this.height = h;
        }
    }

    print() {
        if (this.width === null || this.height === null) {
            console.log("Empty Object");
        } else {
            // Print the rectangle using the character X
            for (let i = 0; i < this.height; i++) {
                console.log("X".repeat(this.width));
            }
        }
    }
}


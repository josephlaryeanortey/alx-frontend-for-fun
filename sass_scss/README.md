# Sass/SCSS Tasks

![Sass/SCSS Logo](https://sass-lang.com/assets/img/logos/logo-b6e1ef6e.svg)

This repository contains a series of advanced tasks designed to practice and demonstrate proficiency in Sass/SCSS. Each task focuses on different features of Sass/SCSS, such as variables, mixins, nesting, loops, and media queries.

## Table of Contents

1. [Task 0: Always debugging!](#task-0-always-debugging)
2. [Task 1: Color variable](#task-1-color-variable)
3. [Task 2: Colors](#task-2-colors)
4. [Task 3: Nested tag](#task-3-nested-tag)
5. [Task 4: Nested class](#task-4-nested-class)
6. [Task 5: Nested child](#task-5-nested-child)
7. [Task 6: Nested hover](#task-6-nested-hover)
8. [Task 7: Nested and nested again](#task-7-nested-and-nested-again)
9. [Task 8: Margin mixin](#task-8-margin-mixin)
10. [Task 9: Extended](#task-9-extended)
11. [Task 10: Import colors](#task-10-import-colors)
12. [Task 11: For each](#task-11-for-each)
13. [Task 12: Loop Headers](#task-12-loop-headers)
14. [Task 13: Columns and operators](#task-13-columns-and-operators)
15. [Task 14: Media query #0](#task-14-media-query-0)
16. [Task 15: Media query #1](#task-15-media-query-1)

---

## Task 0: Always debugging!

Write a Sass file that prints `Hello world` in the debug output.

**File:** `0-debug_log.scss`

---

## Task 1: Color variable

Assign the text color `#3D3D3D` to the `body` and `p` tags using a Sass variable.

**File:** `1-color_variable.scss`

---

## Task 2: Colors

- Assign the text color `#3D3D3D` to `body` and `p` tags.
- Assign the background color `#6D6D6D` to `body` and `h2` tags.
- Use two Sass variables.

**File:** `2-color_variables.scss`

---

## Task 3: Nested tag

- Set `margin` and `padding` of `body` tags to `0`.
- Set `margin` to `10px` for `p` tags inside `body` tags using nested declarations.

**File:** `3-nested_tag.scss`

---

## Task 4: Nested class

- Assign text color `#3D3D3D` to elements inside `body`.
- Assign text color `#FF0000` to `.red` class elements inside `body`.

**File:** `4-nested_class.scss`

---

## Task 5: Nested child

- Assign text color `#3D3D3D` to elements inside `body`.
- Assign text color `#FF0000` to `.red` class elements that are direct children of `body`.

**File:** `5-nested_child.scss`

---

## Task 6: Nested hover

- Set text color `#FF0000` for `button` tags.
- Change text color to `#00FF00` when hovered over.

**File:** `6-nested_hover.scss`

---

## Task 7: Nested and nested again

- Set font size to `14px` for `body`.
- Set font size to `16px` for `h1` inside `body`.
- Set font size to `12px` for `h1.smaller` inside `body`.

**File:** `7-nested_deeper.scss`

---

## Task 8: Margin mixin

- Create a mixin for margins.
- Assign `10px` margin left and right to `body`.
- Assign `15px` margin left and right to `div`.

**File:** `8-mixin_margins.scss`

---

## Task 9: Extended

- Assign font size `12px` to `.info` class.
- Extend `.info` for `.success` and `.warning`.
- Assign text color `#00FF00` to `.success` and `#FF0000` to `.warning`.

**File:** `9-extend_list.scss`

---

## Task 10: Import colors

- Import colors from `10-colors.scss`.
- Assign `$red`, `$green`, and `$blue` to `.red`, `.green`, and `.blue`, respectively.

**File:** `10-import_colors.scss`

---

## Task 11: For each

- Use a list of names to dynamically create classes.
- Assign background images based on the names.

**File:** `11-loop_photos.scss`

---

## Task 12: Loop Headers

- Use a `@for` loop to create `h1` to `h5` tags.
- Assign font sizes `1px` to `5px` respectively.

**File:** `12-loop_header.scss`

---

## Task 13: Columns and operators

- Use variables and arithmetic operations to calculate column sizes dynamically.

**File:** `13-columns.scss`

---

## Task 14: Media query #0

- Create a media query for screen widths of `768px` or less.
- Assign a different background color to `body`.

**File:** `14-media_query_0.scss`

---

## Task 15: Media query #1

- Create a media query for screen widths between `768px` and `1024px`.
- Adjust font sizes for headers.

**File:** `15-media_query_1.scss`

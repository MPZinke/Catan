import { DIRECTIONS } from "../Globals.js";
export class Hexagon {
    constructor(center_x, center_y, height, padding) {
        this.x = center_x;
        this.y = center_y;
        this.height = height;
        this.padding = padding;
        this.radius = height * Hexagon.TWO_OVER_SQUAREROOT_3;
        const radius_cos60 = this.radius * Hexagon.COS60;
        this.points = Array(6);
        this.points[Hexagon.Corners.TOP_LEFT] = [this.x - radius_cos60, this.y - height];
        this.points[Hexagon.Corners.TOP_RIGHT] = [this.x + radius_cos60, this.y - height];
        this.points[Hexagon.Corners.RIGHT] = [this.x + this.radius, this.y];
        this.points[Hexagon.Corners.BOTTOM_RIGHT] = [this.x + radius_cos60, this.y + height];
        this.points[Hexagon.Corners.BOTTOM_LEFT] = [this.x - radius_cos60, this.y + height];
        this.points[Hexagon.Corners.LEFT] = [this.x - this.radius, this.y];
    }
    point_in_hexagon(x, y) {
        if (x < this.x - this.radius || this.x + this.radius < x) {
            return false;
        }
        if (y < this.y - this.height || this.y + this.height < y) {
            return false;
        }
        if (x < this.points[0][0] || this.points[1][0] < x) {
            let x1;
            let x2;
            let y1;
            let y2;
            if (y <= this.y) {
                y1 = this.y - this.height;
                y2 = this.y;
                if (x < this.points[0][0]) {
                    x1 = this.points[0][0];
                    x2 = this.x - this.radius;
                }
                else {
                    x1 = this.points[1][0];
                    x2 = this.x + this.radius;
                }
            }
            else {
                y1 = this.y;
                y2 = this.y + this.height;
                if (x < this.points[0][0]) {
                    x1 = this.x - this.radius;
                    x2 = this.points[4][0];
                }
                else {
                    x1 = this.x + this.radius;
                    x2 = this.points[3][0];
                }
            }
            const slope = this.height / (x2 - x1);
            const y_value_for_x = slope * (x - x1) + y1;
            if (y > this.y) {
                return y <= y_value_for_x;
            }
            else {
                return y_value_for_x <= y;
            }
        }
        return true;
    }
}
Hexagon.COS60 = 0.5;
Hexagon.SIN60 = 0.8660254037844386;
Hexagon.SQUAREROOT_3 = 1.7320508076;
Hexagon.TWO_OVER_SQUAREROOT_3 = 1.1547005384;
Hexagon.Corners = DIRECTIONS["Side's Corners"];

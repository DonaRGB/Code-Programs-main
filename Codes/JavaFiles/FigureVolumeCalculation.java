class Figure {
    public double getVolume() {
        return 0;
    }
}
class Cube extends Figure {
    private double edge;
    public Cube(double edge) {
        this.edge = edge;
    }
    public double getVolume() {
        return edge * edge * edge;
    }
}
class Cylinder extends Figure {
    private double radius;
    private double height;
    public Cylinder(double radius,double height) {
        this.radius = radius;
        this.height = height;
    }
    public double getVolume() {
        return Math.PI * radius * radius * height;
    }
}
class Cuboid extends Figure {
    private double length;
    private double width;
    private double height;
    public Cuboid(double length,double width,double height) {
        this.length = length;
        this.width = width;
        this.height = height;
    }
    public double getVolume() {
        return length * width * height;
    }
}
class Sphere extends Figure {
    private double radius;
    public Sphere(double radius) {
        this.radius = radius;
    }
    public double getVolume() {
        return (4.0 * Math.PI * radius * radius * radius) / 3.0;
    }
}
class Pyramid extends Figure {
    private double length;
    private double width;
    private double height;
    public Pyramid(double length, double width, double height) {
        this.length = length;
        this.width = width;
        this.height = height;
    }
    public double getVolume() {
        return (length * width * height) / 3.0;
    }
}
class Cone extends Figure {
    private double radius;
    private double height;
    public Cone(double radius, double height) {
        this.radius = radius;
        this.height = height;
    }
    public double getVolume() {
        return (Math.PI * radius * radius * height) / 3.0;
    }
}
class Torus extends Figure {
    private double thickness;
    private double inner_radius;
    public Torus(double thickness,double inner_radius) {
        this.thickness = thickness;
        this.inner_radius = inner_radius;
    }
    public double getVolume() {
        return 2 * Math.PI * Math.PI * inner_radius * thickness * thickness;
    }
}
class Tetrahedron extends Figure {
    private double edge_length_tet;
    public Tetrahedron(double edge_length_tet) {
        this.edge_length_tet = edge_length_tet;
    }
    public double getVolume() {
        return (edge_length_tet * edge_length_tet * edge_length_tet) / (6 * Math.sqrt(2));
    }
}
class Octohedron extends Figure {
    private double edge_length_oct;
    public Octohedron(double edge_length_oct) {
        this.edge_length_oct = edge_length_oct;
    }
    public double getVolume() {
        return (Math.sqrt(2) / 3) * (edge_length_oct * edge_length_oct * edge_length_oct);
    }
}
class Dodecahedron extends Figure {
    private double edge_length_dod;
    public Dodecahedron(double edge_length_dod) {
        this.edge_length_dod = edge_length_dod;
    }
    public double getVolume() {
        return ((15 + (7 * Math.sqrt(5))) / 4) * edge_length_dod * edge_length_dod * edge_length_dod;
    }
}
class Icosahedron extends Figure {
    private double edge_length_ico;
    public Icosahedron(double edge_length_ico) {
        this.edge_length_ico = edge_length_ico;
    }
    public double getVolume() {
        return ((5 * (3 + Math.sqrt(5))) / 12) * edge_length_ico * edge_length_ico * edge_length_ico;
    }
}
public class FigureVolumeCalculation { //all units are cm
    public static void main(String[] args) {
        Figure[] s = new Figure[11];
        s[0] = new Cube(5);
        s[1] = new Cylinder(5,4);
        s[2] = new Cuboid(2,3,4);
        s[3] = new Sphere(3);
        s[4] = new Pyramid(5,4,6);
        s[5] = new Cone(3,5);
        s[6] = new Torus(3,6);
        s[7] = new Tetrahedron(3);
        s[8] = new Octohedron(4);
        s[9] = new Dodecahedron(5);
        s[10] = new Icosahedron(6);
        System.out.println("Volume of Cube : " + s[0].getVolume());
        System.out.println("Volume of Cylinder : " + s[1].getVolume());
        System.out.println("Volume of Cuboid : " + s[2].getVolume());
        System.out.println("Volume of Sphere : " + s[3].getVolume());
        System.out.println("Volume of Pyramid : " + s[4].getVolume());
        System.out.println("Volume of Cone : " + s[5].getVolume());
        System.out.println("Volume of Torus : " + s[6].getVolume());
        System.out.println("Volume of Tetrahedron : " + s[7].getVolume());
        System.out.println("Volume of Octohedron : " + s[8].getVolume());
        System.out.println("Volume of Dodecahedron : " + s[9].getVolume());
        System.out.println("Volume of Icosahedron : " + s[10].getVolume());
    }
}
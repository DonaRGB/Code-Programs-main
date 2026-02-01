class Course {
    private String name;
    private int credits;
    private double grade;
    public Course(String name, int credits) {
        this.name = name;
        this.credits = credits;
    }
    public void setGrade(double grade) {
        this.grade = grade;
    }
    public double getGrade() {
        return grade;
    }
    public int getCredits() {
        return credits;
    }
    public String getName() {
        return name;
    }
    public String getLetterGrade() {
        if (grade >= 4.0) return "A";
        else if (grade >= 3.7) return "A-";
        else if (grade >= 3.3) return "B+";
        else if (grade >= 3.0) return "B";
        else if (grade >= 2.7) return "B-";
        else return "C";
    }
}
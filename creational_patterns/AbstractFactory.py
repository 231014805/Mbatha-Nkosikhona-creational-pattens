from abc import ABC, abstractmethod

# Abstract Factory
class UIAbstractFactory(ABC):
    """
    Abstract Factory for creating UI components.
    """

    @abstractmethod
    def create_dashboard(self):
        """Creates a dashboard specific to the user type."""
        pass

    @abstractmethod
    def create_profile_section(self):
        """Creates a profile section specific to the user type."""
        pass


# Concrete Factory for Student
class StudentUIFactory(UIAbstractFactory):
    def create_dashboard(self):
        return StudentDashboard()

    def create_profile_section(self):
        return StudentProfileSection()


# Concrete Factory for Counselor
class CounselorUIFactory(UIAbstractFactory):
    def create_dashboard(self):
        return CounselorDashboard()

    def create_profile_section(self):
        return CounselorProfileSection()


# Abstract Products
class Dashboard(ABC):
    @abstractmethod
    def display(self):
        pass


class ProfileSection(ABC):
    @abstractmethod
    def display(self):
        pass


# Concrete Products for Student
class StudentDashboard(Dashboard):
    def display(self):
        print("Displaying Student Dashboard: View appointments, notifications, and feedback.")


class StudentProfileSection(ProfileSection):
    def display(self):
        print("Displaying Student Profile: Update personal details and preferences.")


# Concrete Products for Counselor
class CounselorDashboard(Dashboard):
    def display(self):
        print("Displaying Counselor Dashboard: View schedule, manage availability, and track sessions.")


class CounselorProfileSection(ProfileSection):
    def display(self):
        print("Displaying Counselor Profile: Update specialization and availability.")


# Client Code
def get_ui_components(factory: UIAbstractFactory):
    """
    Retrieves and displays UI components using the provided factory.
    """
    dashboard = factory.create_dashboard()
    profile_section = factory.create_profile_section()

    dashboard.display()
    profile_section.display()


if __name__ == "__main__":
    # Create UI for Student
    print("Generating UI for Student:")
    student_factory = StudentUIFactory()
    get_ui_components(student_factory)

    print("\nGenerating UI for Counselor:")
    # Create UI for Counselor
    counselor_factory = CounselorUIFactory()
    get_ui_components(counselor_factory)


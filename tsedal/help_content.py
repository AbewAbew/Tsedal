"""Public Tsedal guides. These pages never expose site or user data."""

GUIDES = {
    "introduction": ("Welcome to Tsedal", [
        "Tsedal is your learning space for courses, lessons, assessments and certificates.",
        "Browse the course catalogue to see what is available. Sign in with your Tsedal account to enroll and save your progress. Availability depends on each course's publication and access settings.",
        "Choose the Student Guide for learning help or the Administrator Guide for managing courses and learners.",
    ]),
    "guest": ("Explore Tsedal", [
        "Open the course catalogue to browse published courses and read their descriptions.",
        "Use Log in to access your Tsedal account. If account registration is unavailable, ask your Tsedal administrator for an invitation.",
        "You will need an account to enroll, submit assessments and keep your learning progress. Public previews depend on the course settings.",
    ]),
    "student": ("Tsedal Student Guide", [
        "Sign in to Tsedal, open Courses, and select a course. Follow its enrollment instructions; some courses require payment, an invitation or approval.",
        "Open a chapter and work through its lessons. Use the lesson's completion controls to record progress, and complete any required quizzes or assignments.",
        "Use your profile to update your name, picture and learning information. Check batches for scheduled activities when you have been added to a batch.",
        "Certificates are available only when a course or batch offers them and its completion requirements have been met. Contact your instructor about course access, assessment results or certificates.",
        "If you cannot sign in, use the password-reset option. If a reset email does not arrive, contact your Tsedal administrator.",
    ]),
    "administrator": ("Tsedal Administrator Guide", [
        "Use an authorized administrator or moderator account to manage Tsedal. The sidebar and Settings show the features your account can access.",
        "Create a course, organize chapters and lessons, add assessments, then review publication and enrollment settings before sharing it with students.",
        "Invite members and assign only the roles they need. Use batches to organize groups and scheduled learning activities.",
        "Review completion and assessment results before issuing certificates. Test the published course with a student account before launch.",
        "Email, live-class integrations and payment gateways require separate configuration. Back up Tsedal before making major changes or installing updates.",
    ]),
    "setting-up": ("Set up Tsedal", [
        "Sign in with an administrator account and open Settings. Review your site name, branding, learner access and enabled features.",
        "Invite instructors and students, prepare your first course, and check the experience with a student account.",
        "Ask the site operator to configure the public domain, HTTPS, email delivery and backups before opening Tsedal to the public.",
    ]),
    "create-a-course": ("Create a course in Tsedal", [
        "Open Courses with an instructor or moderator account and use the course creation action.",
        "Enter the course title, description and other required details. Add chapters, lessons and any assessments.",
        "Review the course settings, access rules and instructors. Publish only after checking that the material is ready for learners.",
    ]),
    "add-a-chapter": ("Add a chapter", [
        "Open a course you can edit. Use its course outline to add a chapter and give it a clear title.",
        "Group related lessons in the chapter and arrange them in the order students should follow. Save your changes and review the outline.",
    ]),
    "add-a-lesson": ("Add a lesson", [
        "Open a chapter in a course you can edit and add a lesson. Enter a descriptive title and prepare the lesson content.",
        "Add supporting media or assessments where appropriate. Check links, uploaded files and the lesson preview before publishing.",
    ]),
    "create-a-batch": ("Create a batch", [
        "Open Batches with an authorized account and create a batch. Set its title, schedule and other required details.",
        "Add relevant courses, instructors and students. Review the batch's visibility, capacity and access settings before sharing it.",
    ]),
    "create-a-live-class": ("Schedule a live class", [
        "Open the batch you manage and use its live-class scheduling controls. Set the topic, date, time and meeting details.",
        "Confirm the meeting provider is configured and students can access the session. Check timezone and notification settings before announcing the class.",
    ]),
    "add-a-program": ("Build a learning path", [
        "When Programs is enabled, use an authorized account to create a program and add its courses.",
        "Arrange the learning sequence and review access requirements. Confirm that students can reach every course included in the path.",
    ]),
    "quizzes": ("Quizzes in Tsedal", [
        "Instructors can create quizzes with questions, answer choices and scoring rules, then include them in lessons.",
        "Students should read the instructions and any attempt or time limits before starting. Submit the quiz to receive the results made available by the instructor.",
    ]),
    "assignments": ("Assignments in Tsedal", [
        "Instructors can create assignments with clear instructions and the required submission format.",
        "Students should submit their work through the assignment page and check for evaluation or feedback. Ask the instructor if a submission needs correction.",
    ]),
    "issue-a-certificate": ("Issue a Tsedal certificate", [
        "Review the learner's completion and assessment requirements before issuing a certificate.",
        "Use the certificate controls available for the course or batch. Check the student's name, course details and issue date before sharing the certificate.",
        "Certificate availability depends on the course configuration. Contact the site operator if document export is unavailable.",
    ]),
    "custom-certificate-templates": ("Customize certificate templates", [
        "Authorized administrators can configure certificate templates for Tsedal courses and batches.",
        "Include the learner name, learning achievement, issue date and appropriate Tsedal branding. Preview and test the template before using it for real certificates.",
    ]),
    "setting-up-payment-gateway": ("Configure course payments", [
        "Paid enrollment requires a supported payment provider and an administrator to configure its credentials and currency settings.",
        "Keep provider credentials private. Test enrollment, payment confirmation and failure handling before enabling paid courses for learners.",
        "If a payment or enrollment fails, contact your Tsedal administrator with the transaction reference; never send passwords or full card details.",
    ]),
    "roles": ("Tsedal roles and access", [
        "Students learn and submit their own work. Instructors prepare and teach courses. Moderators and administrators manage the platform according to their assigned permissions.",
        "Administrators should assign the minimum access each person needs. A missing menu item may mean the feature is disabled or the account lacks permission.",
        "Contact your Tsedal administrator to request access. Do not share administrator accounts.",
    ]),
    "about": ("About Tsedal", [
        "Tsedal is a digital learning platform for courses, guided learning and skills development.",
        "This help center covers the Tsedal experience for visitors, students, instructors and administrators.",
    ]),
}

SECTIONS = [
    ("Start here", ["introduction", "guest", "student", "administrator"]),
    ("Manage learning", ["setting-up", "create-a-course", "add-a-chapter", "add-a-lesson",
                         "create-a-batch", "create-a-live-class", "add-a-program"]),
    ("Assessments and certificates", ["quizzes", "assignments", "issue-a-certificate",
                                     "custom-certificate-templates"]),
    ("Platform", ["roles", "setting-up-payment-gateway", "about"]),
]

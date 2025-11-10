import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Unit 5: Expert Systems & AI Programming", layout="wide", page_icon="🤖")

# Sidebar navigation
st.sidebar.title("📚 Navigation")
section = st.sidebar.radio(
    "Select Topic:",
    ["Introduction", "Expert Systems Overview", "ES Components", "ES Development", 
     "ES Applications", "Prolog Programming", "LISP Programming", "Quiz & Summary"]
)

# Main title
st.title("🤖 Unit 5: Expert Systems & AI Programming Languages")
st.markdown("---")

# ============ SECTION 1: INTRODUCTION ============
if section == "Introduction":
    st.header("📖 Introduction to the Unit")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("What You'll Learn")
        st.markdown("""
        This unit covers two major topics:
        
        **1. Expert Systems:**
        - Definition and architecture
        - Components and working principles
        - Knowledge representation
        - Development process
        - Real-world applications
        
        **2. AI Programming Languages:**
        - **Prolog**: Logic-based programming
        - **LISP**: List processing language
        """)
    
    with col2:
        st.subheader("Why This Matters")
        st.info("""
        🎯 **Expert Systems** are crucial for:
        - Medical diagnosis
        - Financial decision-making
        - Manufacturing automation
        - Problem-solving in specialized domains
        
        💻 **Prolog & LISP** are foundational for:
        - AI research and development
        - Natural language processing
        - Knowledge representation
        - Symbolic computation
        """)

# ============ SECTION 2: EXPERT SYSTEMS OVERVIEW ============
elif section == "Expert Systems Overview":
    st.header("🧠 Expert Systems Overview")
    
    # Definition
    st.subheader("What is an Expert System?")
    st.markdown("""
    An **Expert System (ES)** is a computer program designed to solve complex problems and provide 
    decision-making ability like a human expert by extracting knowledge from its knowledge base using 
    reasoning and inference rules.
    """)
    
    # Timeline
    st.info("📅 First expert system developed in **1970** - the first successful AI approach")
    
    # Key Points
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔑 Key Features")
        st.markdown("""
        - Solves domain-specific complex problems
        - Uses facts and heuristics
        - Knowledge stored in Knowledge Base (KB)
        - Performance improves with more knowledge
        - Assists (not replaces) human experts
        - No human thinking capabilities
        """)
    
    with col2:
        st.subheader("📊 Examples")
        examples_df = pd.DataFrame({
            "System": ["DENDRAL", "MYCIN", "PXDES", "CaDeT"],
            "Domain": ["Chemistry", "Medicine", "Oncology", "Cancer Detection"],
            "Purpose": [
                "Detect unknown organic molecules",
                "Diagnose bacterial infections",
                "Determine lung cancer type/level",
                "Early cancer detection"
            ]
        })
        st.dataframe(examples_df, use_container_width=True)
    
    # Characteristics
    st.subheader("✨ Characteristics of Expert Systems")
    char_cols = st.columns(4)
    
    with char_cols[0]:
        st.metric("High Performance", "✓", help="Solves complex problems efficiently")
    with char_cols[1]:
        st.metric("Understandable", "✓", help="Human-readable input/output")
    with char_cols[2]:
        st.metric("Reliable", "✓", help="Accurate outputs")
    with char_cols[3]:
        st.metric("Fast Response", "✓", help="Quick query resolution")
    
    # Example - Google Spell Check
    st.success("💡 **Real-world Example**: Google's spelling correction suggestion is an expert system!")

# ============ SECTION 3: COMPONENTS ============
elif section == "ES Components":
    st.header("🔧 Components of Expert Systems")
    
    # Architecture diagram representation
    st.subheader("System Architecture")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 1️⃣ User Interface")
        st.info("""
        **Purpose**: Interaction layer
        
        - Takes user queries
        - Presents in readable format
        - Passes to inference engine
        - Displays results to user
        - Helps non-experts use the system
        """)
    
    with col2:
        st.markdown("### 2️⃣ Inference Engine")
        st.warning("""
        **Purpose**: Brain of ES
        
        - Main processing unit
        - Applies inference rules
        - Derives conclusions
        - Extracts from KB
        
        **Types:**
        - Deterministic (fact-based)
        - Probabilistic (probability-based)
        """)
    
    with col3:
        st.markdown("### 3️⃣ Knowledge Base")
        st.success("""
        **Purpose**: Storage system
        
        - Stores expert knowledge
        - Contains facts & rules
        - Domain-specific information
        - Bigger KB = Better performance
        """)
    
    # Inference Modes
    st.subheader("🔄 Inference Engine Modes")
    
    tab1, tab2 = st.tabs(["Forward Chaining", "Backward Chaining"])
    
    with tab1:
        st.markdown("""
        ### Forward Chaining (Data-Driven)
        - Starts from **known facts**
        - Applies inference rules
        - Adds conclusions to facts
        - Moves towards goal
        
        **Example**: Given symptoms → Diagnose disease
        """)
    
    with tab2:
        st.markdown("""
        ### Backward Chaining (Goal-Driven)
        - Starts from **goal/hypothesis**
        - Works backward
        - Proves known facts
        - Validates hypothesis
        
        **Example**: Test if patient has disease X → Check symptoms
        """)
    
    # Knowledge Base Components
    st.subheader("📚 Knowledge Base Components")
    
    kb_col1, kb_col2 = st.columns(2)
    
    with kb_col1:
        st.markdown("""
        **Factual Knowledge**
        - Based on facts
        - Accepted by knowledge engineers
        - Objective and verifiable
        
        **Example**: "Fever is a symptom"
        """)
    
    with kb_col2:
        st.markdown("""
        **Heuristic Knowledge**
        - Based on practice/experience
        - Ability to guess
        - Evaluation-based
        
        **Example**: "High fever often indicates infection"
        """)
    
    # Knowledge Acquisition
    st.subheader("🎓 Knowledge Acquisition")
    st.markdown("""
    Process of gathering, selecting, and structuring domain knowledge:
    
    **Methods:**
    1. **Expert Systems**: Domain experts provide rules
    2. **Learning from Examples**: Machine learning approach
    3. **Natural Language Processing**: Extract from text
    4. **Semantic Web**: RDF (Resource Description Framework) and OWL (Web Ontology Language)
    5. **Knowledge Representation & Reasoning**: Formal logic systems
    """)
    
    # RDF Example
    with st.expander("🔍 Example: RDF Triple"):
        st.code("""
        Subject: Patient
        Predicate: Has_symptom
        Object: Fever
        
        → Forms directed labeled graph
        """)

# ============ SECTION 4: DEVELOPMENT ============
elif section == "ES Development":
    st.header("🏗️ Expert System Development")
    
    # Development Process
    st.subheader("Development Workflow (MYCIN Example)")
    
    steps = [
        ("1. Knowledge Feeding", "Human experts provide domain knowledge about bacterial infections, symptoms, causes"),
        ("2. KB Update", "MYCIN's knowledge base is updated with expert information"),
        ("3. Problem Input", "Doctor inputs patient details: symptoms, medical history, condition"),
        ("4. Data Collection", "System uses questionnaire to collect additional info (age, gender, etc.)"),
        ("5. Inference Processing", "Applies IF-THEN rules using inference engine on KB facts"),
        ("6. Output Generation", "Provides diagnosis/recommendation through user interface")
    ]
    
    for step, desc in steps:
        st.markdown(f"**{step}**")
        st.write(f"→ {desc}")
        st.markdown("")
    
    # Participants
    st.subheader("👥 Key Participants in Development")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎓 Expert")
        st.info("""
        - Domain specialist
        - Provides knowledge
        - Success depends on their input
        - Specialized in specific field
        """)
    
    with col2:
        st.markdown("### 💻 Knowledge Engineer")
        st.warning("""
        - Gathers knowledge from experts
        - Codifies into system format
        - Translates to formal rules
        - Implements in ES
        """)
    
    with col3:
        st.markdown("### 👤 End-User")
        st.success("""
        - May not be expert
        - Seeks solutions/advice
        - Queries the system
        - Receives recommendations
        """)
    
    # Expert System Shell
    st.subheader("🐚 Expert System Shell")
    
    st.markdown("""
    An **ES Shell** is an ES without domain-specific knowledge - a pre-packaged inference engine.
    
    **Components of Shell:**
    - Knowledge Acquisition subsystem
    - Knowledge Base (empty initially)
    - Inference Mechanism (reasoning engine)
    - Explanation subsystem
    - User Interface
    """)
    
    # Advantages of Shell
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**✅ Advantages of Using Shell:**")
        st.markdown("""
        - Rapid prototyping
        - Focus on content, not structure
        - Reduces required skill level
        - Pre-built infrastructure
        - Faster development
        """)
    
    with col2:
        st.markdown("**🔧 Shell Components:**")
        components_df = pd.DataFrame({
            "Component": ["Knowledge Base", "Reasoning Engine", "Acquisition", "Explanation", "UI"],
            "Function": ["Store knowledge", "Process logic", "Help build KB", "Justify actions", "User interaction"]
        })
        st.dataframe(components_df, use_container_width=True)

# ============ SECTION 5: APPLICATIONS ============
elif section == "ES Applications":
    st.header("🌐 Applications & Analysis")
    
    # Capabilities
    st.subheader("💪 Capabilities of Expert Systems")
    
    cap_cols = st.columns(3)
    
    with cap_cols[0]:
        st.markdown("""
        **Decision Support:**
        - Advising users
        - Decision-making
        - Problem-solving
        """)
    
    with cap_cols[1]:
        st.markdown("""
        **Communication:**
        - Explaining problems
        - Interpreting input
        - Demonstrating devices
        """)
    
    with cap_cols[2]:
        st.markdown("""
        **Analysis:**
        - Predicting results
        - Diagnosing issues
        - Troubleshooting
        """)
    
    # Applications by Domain
    st.subheader("🎯 Applications by Domain")
    
    applications = {
        "Design & Manufacturing": "Physical device design (camera lenses, automobiles)",
        "Knowledge Domain": "Publishing knowledge (tax advisors, consultants)",
        "Finance": "Fraud detection, loan approval decisions, suspicious activity monitoring",
        "Medical Diagnosis": "Disease diagnosis, treatment recommendations (first ES application area)",
        "Planning & Scheduling": "Task planning, resource scheduling, goal achievement"
    }
    
    for domain, desc in applications.items():
        with st.expander(f"📌 {domain}"):
            st.write(desc)
    
    # Advantages vs Limitations
    st.subheader("⚖️ Advantages vs Limitations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✅ Advantages")
        st.success("""
        - Highly reproducible
        - Works in risky/dangerous environments
        - Lower error probability (with correct KB)
        - Steady performance (unaffected by emotions)
        - Very high response speed
        - No memory limitations
        - High efficiency
        - Consider all available facts
        - Regular updates improve performance
        """)
    
    with col2:
        st.markdown("### ❌ Limitations")
        st.error("""
        - Wrong output if KB has wrong knowledge
        - Cannot produce creative solutions
        - High maintenance & development costs
        - Difficult knowledge acquisition
        - Domain-specific (not general purpose)
        - Cannot learn automatically
        - Requires manual updates
        - Not affected by emotions (can be limitation)
        """)
    
    # Why Use Expert Systems?
    st.subheader("🤔 Why Use Expert Systems?")
    
    reasons = [
        "No memory limitations (unlike human experts)",
        "High efficiency with correct knowledge base",
        "Combines knowledge from multiple experts",
        "Consistent performance (not affected by fatigue, emotions)",
        "High security for sensitive queries",
        "Considers all available facts systematically",
        "Available 24/7 without breaks"
    ]
    
    for reason in reasons:
        st.markdown(f"- {reason}")

# ============ SECTION 6: PROLOG ============
elif section == "Prolog Programming":
    st.header("🔷 Prolog Programming")
    
    st.subheader("What is Prolog?")
    st.markdown("""
    **Prolog** (Programming in Logic) is a logic programming language inspired by formal logic.
    
    **Key Features:**
    - Declarative language (what to solve, not how)
    - Logical variables (not like traditional variables)
    - Built-in unification for term manipulation
    - Backtracking control flow
    - Program clauses = data
    - Can be viewed as relational database with rules
    """)
    
    # Basic Syntax
    st.subheader("📝 Basic Syntax")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Terms", "Clauses", "Queries", "Examples"])
    
    with tab1:
        st.markdown("""
        ### Term Types
        
        **1. Constants**
        - Atoms: `john_smith`, `dyspepsia`, `+`, `=/=`
        - Numbers: `0`, `57`, `1.618`, `-13.6`, `2.04e-27`
        
        **2. Variables**
        - Start with uppercase or underscore
        - Examples: `X`, `Gross_pay`, `_257`, `_`
        
        **3. Compound Terms**
        - Functor with arguments
        - Example: `likes(john, mary)`
        - Tree structure: functor at root, arguments as leaves
        """)
        
        st.code("""
% Examples of Prolog terms
atom_example(alpha17).
number_example(3.14159).
variable_example(X).
compound_example(book(dickens, Z, cricket)).
list_example([1, 3, g(a), 7, 9]).
        """, language="prolog")
    
    with tab2:
        st.markdown("""
        ### Clauses: Facts and Rules
        
        **Facts** (unconditional truths):
        ```
        elephant(george).
        elephant(mary).
        ```
        
        **Rules** (conditional statements):
        ```
        elephant(X) :- grey(X), mammal(X), hasTrunk(X).
        ```
        
        **Interpretation:**
        - **Declarative**: "H is provable if G1, G2, ..., Gn are provable"
        - **Procedural**: "To execute H, execute G1, G2, ..., Gn first"
        """)
    
    with tab3:
        st.markdown("""
        ### Queries
        
        Queries test facts and rules:
        
        ```
        ?- elephant(george).
        yes
        
        ?- elephant(jane).
        no
        ```
        """)
    
    with tab4:
        st.code("""
/* Zoo Example */
elephant(george).
elephant(mary).
panda(chi_chi).

dangerous(X) :- big_teeth(X).
dangerous(X) :- venomous(X).

guess(X, tiger) :- stripey(X), big_teeth(X), isaCat(X).
guess(X, koala) :- arboreal(X), sleepy(X).

/* Pairing Example */
male(bertram).
male(percival).
female(lucinda).
female(camilla).

pair(X, Y) :- male(X), female(Y).

% Query examples:
% ?- pair(percival, X).     % Finds female pairs
% ?- pair(X, lucinda).      % Finds male pairs
% ?- pair(X, Y).            % Finds all pairs
        """, language="prolog")
    
    # Program Structure
    st.subheader("🏗️ Program Structure")
    
    st.markdown("""
    - Programs consist of **procedures**
    - Procedures consist of **clauses**
    - Each clause is a **fact** or **rule**
    - Programs executed by posing **queries**
    """)
    
    # Operators
    st.subheader("🔧 Operators")
    
    operators_df = pd.DataFrame({
        "Position": ["Prefix", "Infix", "Postfix"],
        "Operator Syntax": ["-2", "5+17", "N!"],
        "Normal Syntax": ["-(2)", "+(17,5)", "!(N)"],
        "Example": ["Negation", "Addition", "Factorial"]
    })
    st.table(operators_df)
    
    st.info("""
    **Operator Properties:**
    - **Associativity**: left, right, or none (e.g., X+Y+Z parsed as (X+Y)+Z)
    - **Precedence**: integer value (e.g., X+Y*Z parsed as X+(Y*Z))
    """)

# ============ SECTION 7: LISP ============
elif section == "LISP Programming":
    st.header("🔶 LISP Programming")
    
    st.subheader("What is LISP?")
    st.markdown("""
    **LISP** (LISt Processing) is the second-oldest high-level programming language (1958, MIT by John McCarthy).
    
    **Key Features:**
    - Expression and function-oriented
    - Every procedure is a function returning data objects
    - Machine-independent
    - Iterative design methodology
    - Dynamic program updates
    - High-level debugging
    - Object-oriented programming support
    - Rich data type support
    """)
    
    # Basic Syntax
    st.subheader("📝 Basic Syntax & Examples")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Basics", "Predicates", "Data Types", "Functions", "Operations"])
    
    with tab1:
        st.markdown("""
        ### Syntax Rules
        
        **Comments:**
        ```
        ;this is a comment
        ```
        
        **Output:**
        ```
        (write-line "Hello")
        ```
        
        **Naming Conventions:**
        - Alphanumeric characters (no whitespace)
        - No parentheses, quotes, backslash, comma, colon, semicolon
        - Cannot start with digit
        - Examples: `hello`, `hello99`, `hello_Geek`, `hello123`
        
        **Prefix Notation:**
        ```
        (+ 7 9 11)          ; Sum of 7, 9, 11
        (/ (* a (+ b c)) d) ; a * (b + c) / d
        ```
        """)
    
    with tab2:
        st.markdown("""
        ### Common Predicates
        
        Predicates test conditions and return T (true) or NIL (false).
        """)
        
        predicates_df = pd.DataFrame({
            "Predicate": ["atom", "equal", "eq", "evenp", "oddp", "zerop", 
                         "null", "listp", "numberp", "integerp"],
            "Test": ["Is atom?", "Structural equality", "Object identity", 
                    "Is even?", "Is odd?", "Is zero?",
                    "Is nil?", "Is list?", "Is number?", "Is integer?"],
            "Example": [
                "(atom 'geeks) → T",
                "(equal '(1 2) '(1 2)) → T",
                "(eq 'a 'a) → T",
                "(evenp 20) → T",
                "(oddp 31) → T",
                "(zerop 0) → T",
                "(null nil) → T",
                "(listp '(1 2)) → T",
                "(numberp 67) → T",
                "(integerp 67) → T"
            ]
        })
        st.dataframe(predicates_df, use_container_width=True)
        
        st.code("""
; Predicate examples
(write (atom 'geeks))    ; T
(write (evenp 20))       ; T
(write (oddp 31))        ; T
(write (zerop 0))        ; T
(write (numberp 67))     ; T
        """, language="lisp")
    
    with tab3:
        st.markdown("""
        ### Data Types
        
        **Scalar Types** (single values):
        - Numbers: integer, float, complex, ratio
        - Characters
        - Symbols
        
        **Data Structures** (multiple values):
        - Arrays
        - Vectors (1D arrays)
        - Strings (character arrays)
        - Lists (linked structures)
        - Bit-vectors
        """)
        
        st.code("""
; Number examples
(setq a 1)                      ; Integer
(setq b 2.0)                    ; Float
(setq c 4.0e2)                  ; Scientific notation
(setq d (complex 1 2))          ; Complex: 1+2i
(setq r 124/2)                  ; Ratio

; Array examples
(setf my-array (make-array '(10)))
(setf (aref my-array 0) 25)     ; Set element

; String examples
(write-line "Hello World")
(write (length "Hello"))        ; 5
(write (subseq "Hello World" 6)) ; "World"
        """, language="lisp")
    
    with tab4:
        st.markdown("""
        ### Functions
        
        **Defining Functions:**
        ```
        (defun function-name (parameters)
          "Optional documentation"
          body-expressions)
        ```
        
        **Parameter Types:**
        - Regular parameters
        - `&optional`: Optional parameters
        - `&rest`: Variable number of arguments
        - `&key`: Keyword parameters
        """)
        
        st.code("""
; Basic function
(defun averagenum (n1 n2 n3 n4)
  (/ (+ n1 n2 n3 n4) 4))

(write (averagenum 10 20 30 40))  ; 25

; Optional parameters
(defun show-members (a b &optional c d)
  (write (list a b c d)))

(show-members 1 2)          ; (1 2 NIL NIL)
(show-members 1 2 3 4)      ; (1 2 3 4)

; Keyword parameters
(defun show-members (&key a b c d)
  (write (list a b c d)))

(show-members :a 1 :c 2 :d 3)  ; (1 NIL 2 3)

; Lambda functions (anonymous)
(write ((lambda (a b c) (+ a b c)) 10 20 30))  ; 60
        """, language="lisp")
    
    with tab5:
        st.markdown("""
        ### Operations
        """)
        
        ops_col1, ops_col2 = st.columns(2)
        
        with ops_col1:
            st.markdown("""
            **Arithmetic:**
            - `+, -, *, /`: Basic operations
            - `mod, rem`: Modulus/remainder
            - `incf, decf`: Increment/decrement
            
            **Comparison:**
            - `=, /=`: Equal, not equal
            - `<, >, <=, >=`: Comparisons
            - `max, min`: Maximum, minimum
            """)
        
        with ops_col2:
            st.markdown("""
            **Logical:**
            - `and, or, not`: Boolean logic
            
            **Bitwise:**
            - `logand, logior`: AND, OR
            - `logxor, lognor`: XOR, NOR
            - `logeqv`: Equivalence
            """)
        
        st.code("""
; Arithmetic
(write (+ 10 20 30))        ; 60
(write (* 5 6))             ; 30
(write (mod 10 3))          ; 1

; Comparison
(write (= 5 5))             ; T
(write (< 3 5))             ; T
(write (max 10 20 30))      ; 30

; List operations
(write (cons 1 2))          ; (1 . 2)
(write (car '(a b c)))      ; A
(write (cdr '(a b c)))      ; (B C)
(write (append '(1 2) '(3 4))) ; (1 2 3 4)
        """, language="lisp")
    
    # Advanced Topics
    st.subheader("🚀 Advanced Topics")
    
    adv_col1, adv_col2 = st.columns(2)
    
    with adv_col1:
        st.markdown("""
        **Recursion:**
        ```
        (defun factorial (n)
          (if (= n 0)
              1
              (* n (factorial (- n 1)))))
        
        (factorial 5)  ; 120
        ```
        """)
    
    with adv_col2:
        st.markdown("""
        **Mapping Functions:**
        ```
        (mapcar '1+ '(1 2 3 4))  ; (2 3 4 5)
        
        (mapcar #'(lambda (x) (* x x)) 
                '(2 3 4))        ; (4 9 16)
        ```
        """)
    
    # Control Structures
    st.subheader("🔄 Control Structures")
    
    control_tab1, control_tab2 = st.tabs(["Decision Making", "Loops"])
    
    with control_tab1:
        st.code("""
; IF statement
(if (> a 20)
    (format t "a is greater than 20")
    (format t "a is not greater than 20"))

; COND (multiple conditions)
(cond ((> a 20) (format t "a > 20"))
      ((= a 20) (format t "a = 20"))
      (t (format t "a < 20")))

; CASE statement
(case day
  (1 (format t "Monday"))
  (2 (format t "Tuesday"))
  (t (format t "Other day")))

; WHEN (single test)
(when (> a 20)
  (format t "a is greater than 20"))
        """, language="lisp")
    
    with control_tab2:
        st.code("""
; DOTIMES (fixed iterations)
(dotimes (i 5)
  (print i))              ; 0 1 2 3 4

; DOLIST (iterate over list)
(dolist (item '(a b c))
  (print item))           ; A B C

; LOOP (simple infinite loop)
(loop
  (print n)
  (setq n (+ n 1))
  (when (> n 5) (return)))

; LOOP FOR (structured iteration)
(loop for x from 1 to 10 by 2 do
  (print x))              ; 1 3 5 7 9

; DO (general iteration)
(do ((i 0 (+ i 1)))
    ((>= i 10) i)
  (print i))
        """, language="lisp")

# ============ SECTION 8: QUIZ & SUMMARY ============
elif section == "Quiz & Summary":
    st.header("📝 Quiz & Summary")
    
    # Quick Quiz
    st.subheader("🎯 Quick Quiz")
    
    with st.form("quiz_form"):
        q1 = st.radio(
            "1. What are the three main components of an Expert System?",
            ["A) Input, Output, Process",
             "B) User Interface, Inference Engine, Knowledge Base",
             "C) Hardware, Software, Network",
             "D) Data, Information, Knowledge"],
            key="q1"
        )
        
        q2 = st.radio(
            "2. Which inference mode starts from known facts and moves towards goals?",
            ["A) Backward Chaining",
             "B) Forward Chaining",
             "C) Lateral Chaining",
             "D) Circular Chaining"],
            key="q2"
        )
        
        q3 = st.radio(
            "3. Which language uses logical variables and backtracking?",
            ["A) Python", "B) Java", "C) Prolog", "D) C++"],
            key="q3"
        )
        
        q4 = st.radio(
            "4. In LISP, what does the 'car' function do?",
            ["A) Returns the last element",
             "B) Returns the first element",
             "C) Removes an element",
             "D) Adds an element"],
            key="q4"
        )
        
        q5 = st.radio(
            "5. What was the first expert system developed?",
            ["A) MYCIN", "B) DENDRAL", "C) CaDeT", "D) PXDES"],
            key="q5"
        )
        
        submitted = st.form_submit_button("Submit Quiz")
        
        if submitted:
            score = 0
            if "B)" in q1: score += 1
            if "B)" in q2: score += 1
            if "C)" in q3: score += 1
            if "B)" in q4: score += 1
            if "B)" in q5: score += 1
            
            st.success(f"Your Score: {score}/5 ({score*20}%)")
            
            if score == 5:
                st.balloons()
                st.success("🎉 Perfect Score! You've mastered the material!")
            elif score >= 3:
                st.info("👍 Good job! Review the missed topics for better understanding.")
            else:
                st.warning("📚 Keep studying! Go through the sections again.")
    
    st.markdown("---")
    
    # Summary
    st.subheader("📚 Unit Summary")
    
    summary_tab1, summary_tab2, summary_tab3 = st.tabs(
        ["Expert Systems", "Prolog", "LISP"]
    )
    
    with summary_tab1:
        st.markdown("""
        ### Expert Systems Key Points
        
        **Definition**: AI programs that solve complex problems using knowledge and reasoning like human experts
        
        **Core Components:**
        1. User Interface - interaction layer
        2. Inference Engine - processing/reasoning brain
        3. Knowledge Base - storage of facts and rules
        
        **Famous Examples:**
        - DENDRAL (chemistry)
        - MYCIN (medical diagnosis)
        - PXDES (lung cancer)
        - CaDeT (cancer detection)
        
        **Characteristics:**
        - High performance, understandable, reliable, responsive
        
        **Inference Modes:**
        - Forward Chaining (data-driven)
        - Backward Chaining (goal-driven)
        
        **Applications:**
        - Medical diagnosis
        - Finance/fraud detection
        - Manufacturing
        - Planning & scheduling
        
        **Advantages:** No memory limits, consistent, 24/7 availability
        
        **Limitations:** Domain-specific, can't learn automatically, expensive
        """)
    
    with summary_tab2:
        st.markdown("""
        ### Prolog Key Points
        
        **Definition**: Logic programming language inspired by formal logic
        
        **Key Features:**
        - Declarative programming (what, not how)
        - Logical variables
        - Built-in unification
        - Backtracking control flow
        - Facts and rules
        
        **Basic Syntax:**
        - Facts: `elephant(george).`
        - Rules: `dangerous(X) :- big_teeth(X).`
        - Queries: `?- elephant(george).`
        
        **Terms:**
        - Constants (atoms, numbers)
        - Variables (uppercase start)
        - Compound terms (functors with arguments)
        
        **Structure:**
        - Programs → Procedures → Clauses (facts/rules)
        - Executed by queries
        
        **Interpretations:**
        - Declarative: "H is true if G1, G2... are true"
        - Procedural: "To execute H, execute G1, G2..."
        """)
    
    with summary_tab3:
        st.markdown("""
        ### LISP Key Points
        
        **Definition**: List Processing language (1958) - second-oldest high-level language
        
        **Key Features:**
        - Expression/function-oriented
        - Prefix notation: `(+ 1 2 3)`
        - Every procedure returns a value
        - Dynamic and extensible
        - Rich data type support
        
        **Data Types:**
        - Numbers (integer, float, complex, ratio)
        - Characters and strings
        - Lists and arrays
        - Symbols
        
        **Common Functions:**
        - `car`: first element
        - `cdr`: rest of list
        - `cons`: construct pair
        - `append`: merge lists
        
        **Predicates:**
        - `atom`, `listp`, `numberp`, etc.
        - Return T or NIL
        
        **Control Structures:**
        - Decision: `if`, `cond`, `case`, `when`
        - Loops: `dotimes`, `dolist`, `loop`, `do`
        
        **Parameters:**
        - Regular, `&optional`, `&rest`, `&key`
        
        **Special Features:**
        - Recursion support
        - Lambda functions
        - Mapping functions (`mapcar`)
        """)
    
    st.markdown("---")
    
    # Comparison Table
    st.subheader("🔄 Prolog vs LISP Comparison")
    
    comparison_df = pd.DataFrame({
        "Aspect": ["Paradigm", "Style", "Syntax", "Main Use", "Variables", "Execution"],
        "Prolog": [
            "Logic Programming",
            "Declarative",
            "Facts & Rules",
            "Knowledge representation",
            "Logical variables",
            "Backtracking"
        ],
        "LISP": [
            "Functional Programming",
            "Expression-based",
            "Prefix notation (S-expressions)",
            "Symbolic computation",
            "Traditional variables",
            "Evaluation"
        ]
    })
    st.table(comparison_df)
    
    # Further Resources
    st.subheader("📖 Further Study Resources")
    
    st.markdown("""
    **Practice Topics:**
    1. Build simple expert systems with IF-THEN rules
    2. Write Prolog programs for logical reasoning
    3. Implement recursive functions in LISP
    4. Explore knowledge representation techniques
    5. Study real-world ES applications
    
    **Key Concepts to Master:**
    - Knowledge acquisition methods
    - Inference engine algorithms
    - Prolog unification and backtracking
    - LISP list manipulation
    - Expert system shells
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>💡 Unit 5: Expert Systems & AI Programming Languages</p>
    <p>Built with Streamlit for interactive learning 📚</p>
</div>
""", unsafe_allow_html=True)

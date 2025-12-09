import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="AI Uncertainty & Reasoning Study Guide",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .concept-box {
        background-color: #E3F2FD;
        padding: 20px;
        border-left: 5px solid #2196F3;
        border-radius: 10px;
        margin: 15px 0;
    }
    .example-box {
        background-color: #FFF3E0;
        padding: 20px;
        border-left: 5px solid #FF9800;
        border-radius: 10px;
        margin: 15px 0;
    }
    .warning-box {
        background-color: #FFEBEE;
        padding: 20px;
        border-left: 5px solid #F44336;
        border-radius: 10px;
        margin: 15px 0;
    }
    .definition-box {
        background-color: #F3E5F5;
        padding: 20px;
        border-left: 5px solid #9C27B0;
        border-radius: 10px;
        margin: 15px 0;
    }
    .formula-box {
        background-color: #E8F5E9;
        padding: 20px;
        border-left: 5px solid #4CAF50;
        border-radius: 10px;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📚 Study Topics")
st.sidebar.markdown("---")

topics = [
    "🏠 Home",
    "1️⃣ Uncertainty Basics",
    "2️⃣ Non-Monotonic Reasoning",
    "3️⃣ Truth Maintenance Systems",
    "4️⃣ JTMS - Justification-Based TMS",
    "5️⃣ LTMS - Logic-Based TMS",
    "6️⃣ ATMS - Assumption-Based TMS",
    "7️⃣ Probabilistic Reasoning",
    "8️⃣ Bayes' Theorem",
    "9️⃣ Bayesian Networks",
    "🔟 Certainty Factors",
    "1️⃣1️⃣ Dempster-Shafer Theory",
    "1️⃣2️⃣ Fuzzy Logic"
]

selected_topic = st.sidebar.radio("Choose a topic:", topics, index=0)

# Progress tracker
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Your Progress")
progress = st.sidebar.progress(0)
st.sidebar.caption("Complete topics to track progress!")

# Main content
def render_home():
    st.markdown('<p class="main-header">🧠 AI Uncertainty & Reasoning Study Guide</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Welcome to your **complete study companion** for AI Uncertainty and Reasoning! 
    This app explains every concept from your PPT in simple, easy-to-understand language.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📖 What You'll Learn")
        st.markdown("""
        **Part 1: Uncertainty & Non-Monotonic Reasoning**
        - Understanding uncertainty in AI
        - Non-monotonic reasoning approaches
        - Default reasoning and minimalistic reasoning
        
        **Part 2: Truth Maintenance Systems**
        - JTMS (Justification-Based)
        - LTMS (Logic-Based)
        - ATMS (Assumption-Based)
        
        **Part 3: Probabilistic Methods**
        - Probability basics
        - Bayes' Theorem and applications
        - Bayesian Networks
        - Certainty Factors
        
        **Part 4: Advanced Topics**
        - Dempster-Shafer Theory
        - Fuzzy Logic systems
        """)
    
    with col2:
        st.markdown("### 🎯 How to Use")
        st.markdown("""
        1. **Select a topic** from the sidebar
        2. **Read carefully** - concepts build on each other
        3. **Study examples** - they clarify theory
        4. **Take your time** - understanding > speed
        5. **Revisit topics** as needed for revision
        
        ### 💡 Study Tips
        - Start with Chapter 1 and go sequentially
        - Focus on understanding, not memorizing
        - Pay attention to examples
        - Color-coded boxes help you identify content types
        - Use formulas as reference, not memorization
        """)
    
    st.markdown("---")
    
    st.markdown("### 🚀 Quick Topic Overview")
    
    with st.expander("📋 Chapter-by-Chapter Guide"):
        st.markdown("""
        **Chapter 1-2:** Foundation - Why uncertainty matters, how beliefs change
        
        **Chapter 3-6:** Truth Maintenance - Systems that track and update beliefs automatically
        
        **Chapter 7-10:** Probability-Based - Mathematical approaches using probability theory
        
        **Chapter 11-12:** Alternative Approaches - Evidence theory and fuzzy reasoning
        """)
    
    st.success("👈 **Ready to start? Choose your first topic from the sidebar!**")

def render_uncertainty_basics():
    st.markdown('<p class="main-header">1️⃣ Uncertainty Basics</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="definition-box"><h3>🎯 What is Uncertainty?</h3><p>In traditional logic (like propositional or first-order logic), we assume everything is <strong>certain</strong> - statements are either <strong>TRUE</strong> or <strong>FALSE</strong>.</p><p>But in the real world, we often face situations where we\'re <strong>not completely sure</strong>. This is <strong>uncertainty</strong>.</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 🤔 Understanding the Problem")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Traditional Logic:**
        ```
        A → B  (If A is true, then B is true)
        ```
        - Clear and certain
        - Works great in mathematics
        - Not flexible enough for real world
        """)
    
    with col2:
        st.markdown("""
        **Real World:**
        ```
        We're NOT sure if A is true
        How do we handle this?
        ```
        - Uncertain information
        - Incomplete data
        - Need special reasoning methods
        """)
    
    st.markdown("### 🌍 Where Does Uncertainty Come From?")
    
    causes_col1, causes_col2, causes_col3 = st.columns(3)
    
    with causes_col1:
        st.markdown("""
        **Sources:**
        - 📰 Unreliable sources
        - 🔬 Experimental errors
        """)
    
    with causes_col2:
        st.markdown("""
        **Technical:**
        - ⚙️ Equipment faults
        - 🌡️ Temperature changes
        """)
    
    with causes_col3:
        st.markdown("""
        **Environmental:**
        - 🌍 Climate variations
        - 🎲 Random events
        """)
    
    st.markdown('<div class="example-box"><h4>💡 Real-Life Examples</h4><ul><li><strong>Weather:</strong> "70% chance of rain tomorrow" - Not certain!</li><li><strong>Medical:</strong> "Patient might have flu or cold" - Multiple possibilities</li><li><strong>Stock Market:</strong> "Price may go up" - Unknown future</li><li><strong>Sports:</strong> "Team A will probably win" - Unpredictable outcome</li></ul></div>', unsafe_allow_html=True)
    
    st.markdown("### 🛠️ Two Main Approaches to Handle Uncertainty")
    
    approach1, approach2 = st.tabs(["Non-Monotonic Reasoning", "Statistical Reasoning"])
    
    with approach1:
        st.markdown("### Non-Monotonic Reasoning")
        st.markdown("""
        **Core Idea:** Conclusions can **change** when new information arrives
        
        **How it works:**
        - Start with incomplete knowledge
        - Make assumptions (default beliefs)
        - Update beliefs when new evidence appears
        - Can **retract** old conclusions
        
        **Example:**
        1. **Initial belief:** "Birds can fly" ✅
        2. **Learn new fact:** "Penguins are birds"
        3. **Updated belief:** "Most birds fly, but penguins don't" ✅
        
        **Key Point:** Old conclusions don't always stay true!
        """)
    
    with approach2:
        st.markdown("### Statistical Reasoning")
        st.markdown("""
        **Core Idea:** Use **numbers** (probabilities) to represent uncertainty
        
        **How it works:**
        - Assign probability values (0 to 1)
        - 0 = impossible
        - 1 = certain
        - 0.7 = 70% likely
        
        **Example:**
        - P(Spam Email) = 0.85 (85% sure it's spam)
        - P(Disease | Symptoms) = 0.30 (30% chance)
        
        **Methods include:**
        - Bayes' Theorem
        - Bayesian Networks
        - Certainty Factors
        - Dempster-Shafer Theory
        """)
    
    st.markdown("### 🎓 Key Takeaways")
    
    st.success("""
    ✅ **Uncertainty is normal** in real-world AI systems
    
    ✅ **Two main approaches:** Change beliefs (non-monotonic) OR use probabilities (statistical)
    
    ✅ **Both are important** and used in different situations
    
    ✅ **This course teaches both** approaches in detail
    """)
    
    st.info("👉 **Next:** Learn about Non-Monotonic Reasoning in detail!")

def render_non_monotonic():
    st.markdown('<p class="main-header">2️⃣ Non-Monotonic Reasoning</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="concept-box"><h3>🔄 The Core Concept</h3><p><strong>Monotonic Logic:</strong> Once you prove something true, adding more facts <strong>never changes</strong> that conclusion.</p><p><strong>Non-Monotonic Logic:</strong> Conclusions can be <strong>withdrawn</strong> when new information appears!</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 📊 Visual Comparison")
    
    comp1, comp2 = st.columns(2)
    
    with comp1:
        st.markdown('<div class="warning-box"><h4>❌ Monotonic (Traditional)</h4><p><strong>Example:</strong></p><code>Facts: All birds fly<br>New: Tweety is a bird<br>→ Tweety flies ✅<br><br>Add more facts...<br>→ Tweety STILL flies ✅<br>(Never changes!)</code></div>', unsafe_allow_html=True)
    
    with comp2:
        st.markdown('<div class="definition-box"><h4>✅ Non-Monotonic</h4><p><strong>Example:</strong></p><code>Facts: Birds typically fly<br>New: Tweety is a bird<br>→ Tweety probably flies ✅<br><br>New: Tweety is a penguin<br>→ Tweety does NOT fly ❌<br>(Belief changed!)</code></div>', unsafe_allow_html=True)
    
    st.markdown("### 🎯 Why Do We Need This?")
    
    st.markdown("""
    **Real-world reasoning requires:**
    - Making assumptions with incomplete information
    - Updating beliefs when we learn more
    - Handling contradictions gracefully
    - Reasoning efficiently without all facts upfront
    """)
    
    st.markdown("### 🧩 Types of Non-Monotonic Reasoning")
    
    st.markdown("---")
    st.markdown("## 1️⃣ Default Reasoning")
    
    st.markdown('<div class="definition-box"><p><strong>Default Reasoning:</strong> Make reasonable assumptions unless proven otherwise</p><p>Think: "Innocent until proven guilty"</p></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Non-Monotonic Logic", "Default Logic"])
    
    with tab1:
        st.markdown("### Non-Monotonic Logic")
        st.markdown("""
        Uses a special operator **M** which means "is consistent with what we know"
        
        **Formula:**
        """)
        st.latex(r"A \land M \space B \rightarrow C")
        st.markdown("""
        **Reading:** If A is true AND assuming B is consistent → conclude C
        
        **Example:**
        """)
        st.latex(r"\forall x \forall y \space Related(x,y) \land M \space Getalong(x,y) \rightarrow WillDefend(x,y)")
        st.markdown("""
        **Translation:** If two people are related AND we can assume they get along 
        → they will defend each other
        """)
        
        st.markdown('<div class="example-box"><h4>🔍 Practical Example</h4><p><strong>Statement:</strong> "My uncle is my relative, and I have no reason to think we don\'t get along"</p><p><strong>Conclusion:</strong> "My uncle will defend me"</p><p><strong>Later:</strong> "I discover my uncle doesn\'t like me"</p><p><strong>New Conclusion:</strong> "My uncle won\'t defend me" (retracted!)</p></div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Default Logic")
        st.markdown("""
        **Form:**
        """)
        st.latex(r"\frac{A : B}{C}")
        st.markdown("""
        **Meaning:** 
        - If **A** is provable
        - AND it's **consistent** to assume **B**
        - THEN conclude **C**
        
        **Example:**
        """)
        st.latex(r"\frac{AdultMale(x) : BaseballPlayer(x)}{Height(x, 5'10'')}")
        st.markdown("""
        **Translation:**
        - If x is an adult male
        - AND it's consistent to assume x plays baseball
        - THEN assume x's height is 5'10"
        
        **Why this works:** Most baseball players are around 5'10"
        
        **But:** If we later learn x is 7 feet tall → retract this assumption!
        """)
    
    st.markdown("---")
    st.markdown("## 2️⃣ Minimalistic Reasoning")
    
    st.markdown('<div class="concept-box"><p><strong>Principle:</strong> Assume as <strong>few things as possible</strong> are true</p><p>Don\'t make unnecessary assumptions!</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 🔄 Dependency Directed Backtracking")
    
    st.markdown("""
    **Problem:** When beliefs change, do we restart everything from scratch?
    
    **Solution:** Only change what's affected by the new information!
    """)
    
    st.markdown('<div class="example-box"><h4>📅 Meeting Scheduling Example</h4><p><strong>Initial Plan:</strong></p><ul><li>Day: Tuesday</li><li>Time: 12:15 PM</li><li>Reason: Everyone is available</li></ul><p><strong>Problem Discovered:</strong> No room available on Tuesday!</p><hr><p><strong>❌ Bad Approach:</strong> Start over, recheck everyone\'s availability for every day and time</p><p><strong>✅ Smart Approach (Dependency Directed):</strong></p><ol><li>Change day to Thursday</li><li>Keep time at 12:15 PM</li><li><strong>Don\'t recheck availability</strong> - assume if Tuesday worked, Thursday works too</li></ol><p><strong>Result:</strong> Much faster! We only changed what needed to change.</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 💡 Why This Matters")
    
    st.info("""
    **Efficiency:** Don't waste time rechecking everything
    
    **Intelligence:** Track which beliefs depend on which assumptions
    
    **Flexibility:** Update only what's necessary when something changes
    """)
    
    st.markdown("---")
    st.markdown("## 3️⃣ Statistical Reasoning")
    
    st.markdown("""
    This approach uses **numbers** to handle uncertainty:
    
    - **Certainty Factors:** Simple numeric belief measures
    - **Bayesian Networks:** Graphical probability models
    - **Dempster-Shafer Theory:** Evidence combination
    
    *(These are covered in later chapters)*
    """)
    
    st.markdown("### 🎓 Summary")
    
    st.success("""
    **Non-Monotonic Reasoning allows AI to:**
    
    ✅ Make educated guesses with incomplete info
    
    ✅ Change its mind when learning new facts
    
    ✅ Reason efficiently using defaults and assumptions
    
    ✅ Handle real-world uncertainty intelligently
    """)
    
    st.info("👉 **Next:** Learn how Truth Maintenance Systems implement non-monotonic reasoning!")

def render_tms_overview():
    st.markdown('<p class="main-header">3️⃣ Truth Maintenance Systems (TMS)</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="definition-box"><h3>🎯 What is a TMS?</h3><p>A <strong>Truth Maintenance System</strong> is like a smart bookkeeper that:</p><ul><li>Keeps track of <strong>what the AI believes</strong></li><li>Remembers <strong>why</strong> it believes each thing (justifications)</li><li><strong>Automatically updates</strong> beliefs when evidence changes</li><li>Maintains <strong>consistency</strong> in the belief system</li></ul></div>', unsafe_allow_html=True)
    
    st.markdown("### 🤔 Why Do We Need TMS?")
    
    st.markdown('<div class="example-box"><h4>The Problem Without TMS</h4><p>Imagine an AI system that believes:</p><ul><li>"The car will start" (based on: engine works, has fuel, battery works)</li></ul><p><strong>New information:</strong> Battery is dead!</p><p><strong>Without TMS:</strong> You manually find all beliefs that depend on the battery and update them one by one 😰</p><p><strong>With TMS:</strong> The system automatically:</p><ol><li>Detects the change</li><li>Finds dependent beliefs</li><li>Updates "car will start" to FALSE</li><li>Propagates changes throughout</li></ol><p><strong>Result:</strong> Automatic, consistent, efficient! 🎉</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 🎯 Core Purpose of TMS")
    
    purposes = st.columns(4)
    
    with purposes[0]:
        st.markdown("""
        **Track**
        📋
        
        Keep record of all beliefs
        """)
    
    with purposes[1]:
        st.markdown("""
        **Justify**
        📝
        
        Remember why we believe things
        """)
    
    with purposes[2]:
        st.markdown("""
        **Update**
        🔄
        
        Change beliefs automatically
        """)
    
    with purposes[3]:
        st.markdown("""
        **Maintain**
        ✅
        
        Ensure consistency
        """)
    
    st.markdown("### 🧩 The Three Types of TMS")
    
    st.markdown("---")
    
    type1, type2, type3 = st.columns(3)
    
    with type1:
        st.markdown('<div class="warning-box"><h3>JTMS</h3><h4>Justification-Based</h4><p><strong>Most Common</strong></p><hr><p><strong>How it works:</strong></p><ul><li>Tracks IN/OUT lists</li><li>Simple bookkeeping</li><li>Treats beliefs as atoms</li></ul><p><strong>Good for:</strong></p><ul><li>General reasoning</li><li>Expert systems</li></ul></div>', unsafe_allow_html=True)
    
    with type2:
        st.markdown('<div class="example-box"><h3>LTMS</h3><h4>Logic-Based</h4><p><strong>More Intelligent</strong></p><hr><p><strong>How it works:</strong></p><ul><li>Like JTMS + logic</li><li>Detects contradictions automatically</li><li>Understands logical relationships</li></ul><p><strong>Good for:</strong></p><ul><li>Logical reasoning</li><li>Diagnosis systems</li></ul></div>', unsafe_allow_html=True)
    
    with type3:
        st.markdown('<div class="definition-box"><h3>ATMS</h3><h4>Assumption-Based</h4><p><strong>Most Powerful</strong></p><hr><p><strong>How it works:</strong></p><ul><li>Explores multiple scenarios at once</li><li>No backtracking needed</li><li>Maintains contexts</li></ul><p><strong>Good for:</strong></p><ul><li>Complex problems</li><li>Multiple hypotheses</li></ul></div>', unsafe_allow_html=True)
    
    st.markdown("### 🔗 How TMS Works: The Dependency Network")
    
    st.markdown('<div class="concept-box"><p>Think of it like a <strong>social network</strong>, but for beliefs:</p><ul><li><strong>Nodes</strong> = Individual beliefs/assertions</li><li><strong>Connections</strong> = Dependencies (what supports what)</li><li><strong>Labels</strong> = Status (believed or not believed)</li></ul><p>When one belief changes, the network automatically updates connected beliefs!</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 📊 Simple Example")
    
    st.markdown("""
    ```
    Belief Network:
    
    [Engine Works] ──┐
                      ├──> [Car Starts]
    [Has Fuel] ───────┤
                      │
    [Battery Works] ──┘
    
    If "Battery Works" becomes FALSE:
    → "Car Starts" automatically becomes FALSE
    → System stays consistent!
    ```
    """)
    
    st.markdown("### 🔑 Key Operations")
    
    operations = {
        'Operation': ['Consistent Labeling', 'Contradiction Resolution', 'Dependency Tracking', 'Belief Propagation'],
        'What it does': [
            'Ensures all beliefs are compatible',
            'Fixes conflicting beliefs',
            'Remembers what depends on what',
            'Spreads changes through network'
        ],
        'Example': [
            'If A supports B, and A is FALSE, then B must be FALSE',
            'Can\'t believe both "raining" and "not raining"',
            '"Car starts" depends on "battery works"',
            'Battery fails → car doesn\'t start → can\'t drive to work'
        ]
    }
    
    df = pd.DataFrame(operations)
    st.table(df)
    
    st.markdown("### ⚡ Benefits of Using TMS")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Advantages:**
        - ✅ Automatic consistency maintenance
        - ✅ Efficient belief updates
        - ✅ Tracks reasoning history
        - ✅ Supports non-monotonic reasoning
        - ✅ Reduces manual work
        """)
    
    with col2:
        st.markdown("""
        **Use Cases:**
        - 🏥 Medical diagnosis systems
        - 🔧 Fault diagnosis
        - 🤖 Planning and scheduling
        - 🧠 Expert systems
        - 🎯 Decision support
        """)
    
    st.markdown("### 🎓 Key Takeaway")
    
    st.success("""
    **TMS is the "autopilot" for managing beliefs in AI systems!**
    
    Instead of manually tracking and updating everything, TMS does it automatically 
    by maintaining a dependency network of beliefs and their justifications.
    
    The next three chapters explore each type in detail! 📚
    """)
    
    st.info("👉 **Next:** Deep dive into JTMS with the ABC Murder Mystery example!")

# Continue with remaining functions...
def render_jtms():
    st.markdown('<p class="main-header">4️⃣ JTMS - Justification-Based TMS</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="concept-box"><h3>🎯 What is JTMS?</h3><p>JTMS is the <strong>simplest and most popular</strong> Truth Maintenance System. It acts as a pure <strong>bookkeeper</strong> that:</p><ul><li>Doesn\'t understand the <strong>meaning</strong> of beliefs</li><li>Just tracks <strong>which beliefs support which</strong></li><li>Maintains <strong>consistent labels</strong> (IN or OUT)</li><li>Lets another system do the actual reasoning</li></ul></div>', unsafe_allow_html=True)
    
    st.markdown("### 🧩 Core Components")
    
    comp1, comp2, comp3 = st.columns(3)
    
    with comp1:
        st.markdown("""
        **Assertions**
        
        Propositions that can be believed
        
        Examples:
        - "Abbott is a suspect"
        - "It's raining"
        - "Battery works"
        """)
    
    with comp2:
        st.markdown("""
        **Justifications**
        
        Reasons WHY we believe something
        
        Has two parts:
        - IN-list (must be true)
        - OUT-list (must be false)
        """)
    
    with comp3:
        st.markdown("""
        **Labels**
        
        Current belief status
        
        Values:
        - IN (believed)
        - OUT (not believed)
        - UNKNOWN
        """)
    
    st.markdown("### 📋 Understanding Justifications")
    
    st.markdown('<div class="definition-box"><h3>The Justification Rule</h3><p>An assertion is <strong>valid (IN)</strong> if and only if:</p><ol><li><strong>ALL</strong> beliefs in the IN-list are IN ✅</li><li><strong>NONE</strong> of the beliefs in the OUT-list are IN ❌</li></ol></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="example-box"><h4>Simple Example: Suspect Abbott</h4><p><strong>Assertion:</strong> "Abbott is a suspect"</p><p><strong>Justification:</strong></p><ul><li><strong>IN-list:</strong> [Beneficiary(Abbott)] - must be true</li><li><strong>OUT-list:</strong> [Alibi(Abbott)] - must be false</li></ul><hr><p><strong>Scenario 1:</strong></p><ul><li>Beneficiary(Abbott) = IN ✅</li><li>Alibi(Abbott) = OUT ❌</li><li><strong>Result:</strong> Suspect(Abbott) = IN ✅</li></ul><p><strong>Scenario 2:</strong></p><ul><li>Beneficiary(Abbott) = IN ✅</li><li>Alibi(Abbott) = IN ✅ (found evidence!)</li><li><strong>Result:</strong> Suspect(Abbott) = OUT ❌ (no longer suspect!)</li></ul></div>', unsafe_allow_html=True)
    
    st.markdown("### 🕵️ The ABC Murder Mystery")
    
    st.markdown('<div class="warning-box"><h4>📖 The Story</h4><p>Someone has been murdered. There are three suspects:</p><ul><li><strong>Abbott</strong></li><li><strong>Babbitt</strong></li><li><strong>Cabot</strong></li></ul><p>All three are <strong>beneficiaries</strong> of the deceased (they inherit money). We need to find the primary suspect by checking their alibis.</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 🔍 Abbott's Investigation")
    
    abbott_col1, abbott_col2 = st.columns(2)
    
    with abbott_col1:
        st.markdown('<div class="example-box"><h4>Initial Situation</h4><p><strong>Facts we have:</strong></p><ul><li>✅ Abbott is a beneficiary</li><li>❌ Abbott has NO alibi (so far)</li></ul><hr><p><strong>Justification for "Suspect(Abbott)":</strong></p><ul><li><strong>IN-list:</strong> Beneficiary(Abbott)</li><li><strong>OUT-list:</strong> Alibi(Abbott)</li></ul><hr><p><strong>Check:</strong></p><ul><li>Beneficiary(Abbott) = IN ✅</li><li>Alibi(Abbott) = OUT ❌</li></ul><p><strong>Conclusion:</strong> Suspect(Abbott) = <span style="color:red">IN ✅</span></p><p><strong>Abbott is our suspect!</strong></p></div>', unsafe_allow_html=True)
    
    with abbott_col2:
        st.markdown('<div class="definition-box"><h4>New Evidence Arrives!</h4><p><strong>Discovery:</strong> Abbott was registered at an Albany hotel at the time of murder!</p><hr><p><strong>Updated facts:</strong></p><ul><li>✅ Abbott is a beneficiary (still true)</li><li>✅ Abbott HAS an alibi (new!)</li></ul><hr><p><strong>Justification check:</strong></p><ul><li>IN-list: Beneficiary(Abbott) = IN ✅</li><li>OUT-list: Alibi(Abbott) = IN ✅ <strong>← PROBLEM!</strong></li></ul><hr><p><strong>New Conclusion:</strong> Suspect(Abbott) = <span style="color:green">OUT ❌</span></p><p><strong>Abbott is NO longer a suspect!</strong></p></div>', unsafe_allow_html=True)
    
    st.markdown("### 📊 Visual Representation")
    
    st.markdown("""
    ```
    Network Diagram for Abbott:
    
    [Beneficiary(Abbott)] ──(+)──┐
                                  │
                                  ├──> [Suspect(Abbott)]
                                  │
    [Alibi(Abbott)] ──────(-)────┘
    
    Legend:
    (+) = IN-list connection (must be believed)
    (-) = OUT-list connection (must NOT be believed)
    ──> = Supports this conclusion
    
    When Alibi changes from OUT to IN:
    → Suspect automatically changes from IN to OUT!
    ```
    """)
    
    st.markdown("### 🔄 What JTMS Does Automatically")
    
    what_does = st.columns(2)
    
    with what_does[0]:
        st.markdown('<div class="concept-box"><h3>✅ JTMS Performs:</h3><ol><li><strong>Consistent Labeling</strong><br>Keeps all labels (IN/OUT) consistent with justifications</li><li><strong>Contradiction Resolution</strong><br>Handles conflicting beliefs</li><li><strong>Automatic Propagation</strong><br>When one belief changes, updates all dependent beliefs</li></ol></div>', unsafe_allow_html=True)
    
    with what_does[1]:
        st.markdown('<div class="warning-box"><h3>❌ JTMS Does NOT:</h3><ol><li><strong>Apply reasoning rules</strong><br>You must tell it what rules to use</li><li><strong>Create justifications</strong><br>You must provide them</li><li><strong>Choose between alternatives</strong><br>You must decide</li><li><strong>Detect contradictions on its own</strong><br>You must flag them</li></ol></div>', unsafe_allow_html=True)
    
    st.markdown("### 🎯 Complete Example: All Three Suspects")
    
    st.markdown("""
    **Let's track all three suspects:**
    
    | Suspect | Beneficiary? | Alibi? | Suspect Status |
    |---------|-------------|--------|----------------|
    | Abbott  | ✅ IN | ✅ IN (hotel) | ❌ OUT (has alibi) |
    | Babbitt | ✅ IN | ✅ IN (brother-in-law) | ❌ OUT (has alibi) |
    | Cabot   | ✅ IN | ✅ IN (ski show) | ❌ OUT (has alibi) |
    
    **Result:** All three have alibis, so none are suspects!
    
    **But wait...** What if one of these alibis is fake? That's where we might need 
    to create a contradiction and let JTMS help us explore alternatives!
    """)
    
    st.markdown("### 💡 Key Insight About JTMS")
    
    st.info("""
    **JTMS is like a smart assistant:**
    
    - **You provide:** The justifications and rules
    - **JTMS handles:** Keeping everything consistent automatically
    
    When evidence changes, JTMS instantly updates all affected beliefs 
    by following the justification network!
    """)
    
    st.markdown("### 🎓 Summary")
    
    st.success("""
    **JTMS Key Points:**
    
    ✅ Simple bookkeeping system for beliefs
    
    ✅ Uses IN-lists and OUT-lists for justifications
    
    ✅ Automatically maintains consistency
    
    ✅ Perfect for non-monotonic reasoning
    
    ✅ Most widely used TMS in practice
    """)
    
    st.info("👉 **Next:** Learn about LTMS, which adds logical intelligence!")

def render_ltms():
    st.markdown('<p class="main-header">5️⃣ LTMS - Logic-Based TMS</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="concept-box"><h3>🎯 What is LTMS?</h3><p>LTMS is like JTMS, but <strong>smarter</strong>! It understands <strong>logical relationships</strong> and can <strong>automatically detect contradictions</strong>.</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 🔄 The Key Difference")
    
    diff_col1, diff_col2 = st.columns(2)
    
    with diff_col1:
        st.markdown('<div class="warning-box"><h3>JTMS</h3><p><strong>Treats beliefs as atoms</strong></p><ul><li>No automatic contradiction detection</li><li>Can label both P and ¬P as IN at the same time</li><li>You must explicitly create contradiction nodes</li><li>Doesn\'t understand logical relationships</li></ul><p><strong>Example:</strong></p><p>Can believe both:</p><ul><li>"Lights are ON" = IN</li><li>"Lights are OFF" = IN</li></ul><p>JTMS won\'t complain!</p></div>', unsafe_allow_html=True)
    
    with diff_col2:
        st.markdown('<div class="definition-box"><h3>LTMS</h3><p><strong>Treats beliefs as logical propositions</strong></p><ul><li><strong>Automatically</strong> detects contradictions</li><li>CANNOT label both P and ¬P as IN</li><li>Understands P and ¬P are opposites</li><li>Uses logical relationships</li></ul><p><strong>Example:</strong></p><p>If you try to believe:</p><ul><li>"Lights are ON" = IN</li><li>"Lights are OFF" = IN</li></ul><p>LTMS <strong>automatically detects</strong> the contradiction!</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 🚗 Car Diagnosis Example")
    
    st.markdown('<div class="example-box"><h4>🎯 The Scenario</h4><p>An expert system is trying to diagnose why a car won\'t start. The mechanic provides observations, and the system maintains beliefs about the car.</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 📊 Step-by-Step Process")
    
    step1, step2, step3, step4 = st.tabs(["Step 1: Initial", "Step 2: Contradiction", "Step 3: Backtracking", "Step 4: Resolution"])
    
    with step1:
        st.markdown("### Step 1: Initial Assumptions")
        st.markdown('<div class="concept-box"><p><strong>System starts with these assumptions:</strong></p></div>', unsafe_allow_html=True)
        st.markdown("""
        **Node A:** `engine_is_running_properly` = IN ✅
        - *Justification:* Initial assumption (empty IN-list)
        
        **Node B:** `has_fuel` = IN ✅
        - *Justification:* Initial assumption
        
        **Node C:** `battery_is_working` = IN ✅
        - *Justification:* Initial assumption
        
        **Node D:** `car_starts` = IN ✅
        - *Justification:* IN(A, B, C) - needs all three
        - *Reasoning:* If engine works AND has fuel AND battery works → car starts
        
        **Initial Conclusion:** Car should start! 🚗✅
        """)
    
    with step2:
        st.markdown("### Step 2: Contradiction Arises")
        st.markdown('<div class="warning-box"><p><strong>New Evidence from Mechanic:</strong></p></div>', unsafe_allow_html=True)
        st.markdown("""
        **Observation:** `car_does_not_start` = IN ✅
        - *Justification:* Direct observation (fact)
        
        **Problem Detected:**
        - System believes: `car_starts` = IN ✅
        - New evidence says: `car_does_not_start` = IN ✅
        - **These are logical opposites!**
        
        **LTMS Automatic Response:**
        🚨 **CONTRADICTION DETECTED!** 🚨
        
        *(JTMS would need you to explicitly create a contradiction node)*
        """)
    
    with step3:
        st.markdown("### Step 3: Dependency-Directed Backtracking")
        st.markdown('<div class="definition-box"><p><strong>LTMS traces the problem:</strong></p></div>', unsafe_allow_html=True)
        st.markdown("""
        **Tracing Dependencies:**
        ```
        car_starts (IN) depends on:
        ├── engine_is_running_properly (IN) ✅
        ├── has_fuel (IN) ✅
        └── battery_is_working (IN) ✅
        
        One of these MUST be wrong!
        ```
        
        **Mechanic Tests:**
        - ✅ Engine: Working fine
        - ✅ Fuel: Tank is full
        - ❌ Battery: **DEAD!** 🔋💀
        
        **Discovery:** The battery assumption was wrong!
        """)
    
    with step4:
        st.markdown("### Step 4: Belief Revision")
        st.markdown('<div class="formula-box"><p><strong>LTMS Updates the Network:</strong></p></div>', unsafe_allow_html=True)
        st.markdown("""
        **Update Process:**
        
        1️⃣ **Retract Battery Assumption:**
        - Node C: `battery_is_working` = OUT ❌
        - New justification: OUT(battery_is_dead_evidence)
        
        2️⃣ **Propagate Change:**
        - Node D: `car_starts` = OUT ❌
        - Because one of its dependencies (C) is now OUT
        
        3️⃣ **Add New Belief:**
        - New Node: `battery_is_not_working` = IN ✅
        
        4️⃣ **Update Conclusion:**
        - `car_does_not_start` = IN ✅
        - Consistent with observation!
        
        **System is now consistent!** ✅
        """)
    
    st.markdown("### 🔗 The Complete Flow")
    
    st.markdown("""
    ```
    Initial State:
    [Engine OK] ─┐
    [Fuel OK]   ─┼─> [Car Starts] ✅
    [Battery OK]─┘
    
    ↓ New Evidence: Car doesn't start
    
    Contradiction!
    
    ↓ Test assumptions
    
    [Engine OK] ─┐
    [Fuel OK]   ─┼─> [Car Starts] ❌
    [Battery ❌] ─┘
    
    ↓ Update beliefs
    
    Final State:
    [Engine OK] ─┐
    [Fuel OK]   ─┼─> [Car Doesn't Start] ✅
    [Battery ❌] ─┘
    
    Diagnosis: Battery is dead!
    ```
    """)
    
    st.markdown("### ✨ Key Features of LTMS")
    
    features_col1, features_col2 = st.columns(2)
    
    with features_col1:
        st.markdown("""
        **Intelligence:**
        - 🧠 Logic-aware reasoning
        - 🔍 Automatic contradiction detection
        - 🔗 Understands logical relationships
        - ⚡ Efficient dependency tracking
        """)
    
    with features_col2:
        st.markdown("""
        **Process:**
        - 📋 Maintains dependency network (like JTMS)
        - 🚨 Detects logical contradictions automatically
        - 🔍 Traces back through dependencies
        - ❌ Retracts responsible beliefs
        - 🔄 Propagates changes forward
        """)
    
    st.markdown("### 📊 JTMS vs LTMS Comparison")
    
    comparison = {
        'Feature': [
            'Contradiction Detection',
            'Logical Awareness',
            'P and ¬P both IN',
            'Setup Complexity',
            'Intelligence Level',
            'Best For'
        ],
        'JTMS': [
            'Manual (you create nodes)',
            'None (treats as atoms)',
            'Allowed (no detection)',
            'Simple',
            'Bookkeeping',
            'Simple reasoning tasks'
        ],
        'LTMS': [
            'Automatic',
            'Full (understands logic)',
            'Automatically prevented',
            'Moderate',
            'Logic-based reasoning',
            'Diagnosis, complex reasoning'
        ]
    }
    
    df_comparison = pd.DataFrame(comparison)
    st.table(df_comparison)
    
    st.markdown("### 💡 When to Use LTMS")
    
    st.info("""
    **Use LTMS when:**
    
    ✅ You need automatic contradiction detection
    
    ✅ Working with logical propositions
    
    ✅ Building diagnosis systems
    
    ✅ Logical consistency is critical
    
    ✅ You want smarter reasoning
    """)
    
    st.markdown("### 🎓 Summary")
    
    st.success("""
    **LTMS = JTMS + Logical Intelligence**
    
    ✅ Automatically understands logical relationships
    
    ✅ Detects contradictions without being told
    
    ✅ More powerful for complex reasoning
    
    ✅ Perfect for diagnostic systems
    
    ✅ Efficient dependency-directed backtracking
    """)
    
    st.info("👉 **Next:** Learn about ATMS, which explores multiple worlds at once!")

# Due to length constraints, I'll create the remaining render functions in a concise format

def render_atms():
    st.markdown('<p class="main-header">6️⃣ ATMS - Assumption-Based TMS</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="concept-box"><h3>🎯 What is ATMS?</h3><p>ATMS explores <strong>all possible worlds simultaneously</strong>! Instead of picking one path and backtracking, it maintains <strong>multiple contexts</strong> in parallel.</p></div>', unsafe_allow_html=True)
    
    # Comparison
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="example-box"><h4>JTMS & LTMS</h4><p><strong>Depth-First Approach</strong></p><ul><li>Follow one reasoning path</li><li>Backtrack when wrong</li><li>Serial exploration</li><li>Faster per path</li><li>May redo work</li></ul></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="definition-box"><h4>ATMS</h4><p><strong>Breadth-First Approach</strong></p><ul><li>Explore all paths at once</li><li>No backtracking needed</li><li>Parallel exploration</li><li>More memory usage</li><li>Never redo work</li></ul></div>', unsafe_allow_html=True)
    
    st.markdown("### 🕵️ ABC Murder - ATMS Style")
    
    st.markdown('<div class="example-box"><p><strong>Setup:</strong> Same murder case, but now we explore ALL possibilities at once!</p></div>', unsafe_allow_html=True)
    
    # Assumptions
    st.markdown("### 📋 All Assumptions Defined")
    
    assumptions_col1, assumptions_col2 = st.columns(2)
    
    with assumptions_col1:
        st.markdown("""
        - **A1:** Hotel register forged
        - **A2:** Hotel register NOT forged
        - **A3:** Babbitt's B-I-L lied
        - **A4:** Babbitt's B-I-L did NOT lie
        """)
    
    with assumptions_col2:
        st.markdown("""
        - **A5:** Cabot lied
        - **A6:** Cabot did NOT lie
        - **A7:** Only A,B,C are suspects
        - **A8:** NOT only A,B,C are suspects
        """)
    
    # Contexts
    st.markdown("### 🌍 Valid Contexts (Worlds)")
    
    st.markdown("""
    **After ATMS prunes inconsistent contexts, we have:**
    
    1. **{A7, A1, A4, A6}** → Abbott is prime suspect (register was forged)
    2. **{A7, A2, A3, A6}** → Babbitt is prime suspect (B-I-L lied)
    3. **{A7, A2, A4, A5}** → Cabot is prime suspect (Cabot lied)
    4. **{A8, A2, A4, A6}** → Look elsewhere (all three have alibis)
    
    **Each context represents a consistent possible world!**
    """)
    
    st.markdown("### 🎯 How ATMS Labels Work")
    
    st.markdown('<div class="formula-box"><p><strong>Example Label: {A7, A2, A6}</strong></p><p>Meaning: "This belief is valid in any world where A7 AND A2 AND A6 are all true"</p><p>An assertion can have <strong>multiple labels</strong> representing different contexts!</p></div>', unsafe_allow_html=True)
    
    st.markdown("### ✅ Advantages vs ❌ Disadvantages")
    
    adv_col, dis_col = st.columns(2)
    
    with adv_col:
        st.markdown("""
        **Advantages:**
        - ✅ No backtracking needed
        - ✅ All scenarios explored
        - ✅ Complete picture
        - ✅ Good for complex problems
        """)
    
    with dis_col:
        st.markdown("""
        **Disadvantages:**
        - ❌ High memory usage
        - ❌ Complex implementation
        - ❌ Label management overhead
        - ❌ Slower for simple problems
        """)
    
    st.success("**ATMS = Parallel Universe Explorer!** 🌌")

def render_probabilistic():
    st.markdown('<p class="main-header">7️⃣ Probabilistic Reasoning</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="definition-box"><h3>🎯 What is Probabilistic Reasoning?</h3><p>Instead of saying "definitely true" or "definitely false", we use <strong>numbers between 0 and 1</strong> to express how likely something is!</p></div>', unsafe_allow_html=True)
    
    # Probability basics
    st.markdown("### 📊 Probability Basics")
    
    st.latex(r"0 \leq P(A) \leq 1")
    
    st.markdown("""
    - **P(A) = 0** → Impossible
    - **P(A) = 0.5** → 50-50 chance
    - **P(A) = 1** → Certain
    """)
    
    # Formula
    st.markdown('<div class="formula-box"><p><strong>Basic Formula:</strong></p></div>', unsafe_allow_html=True)
    
    st.latex(r"P(A) = \frac{\text{Favorable outcomes}}{\text{Total outcomes}}")
    
    # Example
    st.markdown('<div class="example-box"><h4>🎲 Die Roll Example</h4><p>Probability of rolling a 6:</p></div>', unsafe_allow_html=True)
    
    st.latex(r"P(\text{six}) = \frac{1}{6} \approx 0.167 = 16.7\%")
    
    # Conditional Probability
    st.markdown("### 🔗 Conditional Probability")
    
    st.latex(r"P(A|B) = \frac{P(A \cap B)}{P(B)}")
    
    st.markdown("**Meaning:** Probability of A given that B happened")
    
    # Student Example
    st.markdown('<div class="example-box"><h4>📚 Student Preferences Example</h4><ul><li>70% like English: P(English) = 0.7</li><li>40% like both: P(English ∩ Math) = 0.4</li></ul><p><strong>Question:</strong> What % of English-lovers also like Math?</p></div>', unsafe_allow_html=True)
    
    st.latex(r"P(\text{Math}|\text{English}) = \frac{0.4}{0.7} = 0.57 = 57\%")
    
    st.success("**57% of students who like English also like Math!**")

def render_bayes():
    st.markdown('<p class="main-header">8️⃣ Bayes\' Theorem</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="concept-box"><h3>🎯 The Power of Bayes</h3><p>Bayes\' Theorem lets us <strong>update beliefs</strong> when we get new evidence. It\'s the foundation of modern AI!</p></div>', unsafe_allow_html=True)
    
    # Formula
    st.markdown("### 📐 The Formula")
    
    st.latex(r"P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}")
    
    st.markdown('<div class="definition-box"><p><strong>Terms:</strong></p><ul><li><strong>P(A|B)</strong> = Posterior (what we want)</li><li><strong>P(B|A)</strong> = Likelihood</li><li><strong>P(A)</strong> = Prior</li><li><strong>P(B)</strong> = Evidence</li></ul></div>', unsafe_allow_html=True)
    
    # Medical Example
    st.markdown("### 🏥 Meningitis Example")
    
    st.markdown('<div class="example-box"><p><strong>Given:</strong></p><ul><li>P(Stiff Neck | Meningitis) = 0.8</li><li>P(Meningitis) = 1/30,000</li><li>P(Stiff Neck) = 0.02</li></ul><p><strong>Find:</strong> P(Meningitis | Stiff Neck) = ?</p></div>', unsafe_allow_html=True)
    
    st.latex(r"P(M|SN) = \frac{0.8 \times 0.0000333}{0.02} = 0.00133 = 0.13\%")
    
    st.success("**Result:** Only 0.13% chance! (1 in 750)")
    st.info("Even though stiff neck is common with meningitis, the disease is so rare that most stiff necks are from other causes!")
    
    # Card Example
    st.markdown("### 🃏 Playing Card Example")
    
    st.markdown('<div class="example-box"><p><strong>Problem:</strong> A card is a face card. What\'s the probability it\'s a King?</p></div>', unsafe_allow_html=True)
    
    st.latex(r"P(\text{King}|\text{Face}) = \frac{1 \times \frac{1}{13}}{\frac{3}{13}} = \frac{1}{3} = 33.3\%")
    
    st.success("**Makes sense:** 4 kings among 12 face cards = 4/12 = 1/3")

def render_bayesian_networks():
    st.markdown('<p class="main-header">9️⃣ Bayesian Networks</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="definition-box"><h3>🎯 What is a Bayesian Network?</h3><p>A <strong>graphical model</strong> showing how variables depend on each other, with probability tables for each relationship.</p></div>', unsafe_allow_html=True)
    
    # Components
    st.markdown("### 🧩 Two Main Components")
    
    comp1, comp2 = st.columns(2)
    
    with comp1:
        st.markdown("""
        **1. Directed Acyclic Graph (DAG)**
        - Nodes = Variables
        - Arrows = Dependencies
        - No cycles allowed
        """)
    
    with comp2:
        st.markdown("""
        **2. Conditional Probability Tables**
        - Each node has a CPT
        - Shows P(Node | Parents)
        - Specifies relationships
        """)
    
    # Burglary Example
    st.markdown("### 🏠 Burglary Alarm Example")
    
    st.markdown("""
    ```
    Burglary    Earthquake
        ↓           ↓
        └→ Alarm ←┘
             ↓
        ┌────┴────┐
        ↓         ↓
    David      Sophia
    Calls      Calls
    ```
    """)
    
    st.markdown('<div class="example-box"><p><strong>Story:</strong> Alarm can go off due to burglary OR earthquake. When it sounds, neighbors David and Sophia may call.</p></div>', unsafe_allow_html=True)
    
    # Probability Tables
    st.markdown("### 📊 Probability Tables")
    
    # Prior probabilities
    prior_col1, prior_col2 = st.columns(2)
    
    with prior_col1:
        st.markdown("**Burglary:**")
        st.write("- P(B=True) = 0.002")
        st.write("- P(B=False) = 0.998")
    
    with prior_col2:
        st.markdown("**Earthquake:**")
        st.write("- P(E=True) = 0.001")
        st.write("- P(E=False) = 0.999")
    
    # Alarm CPT
    alarm_data = {
        'Burglary': ['True', 'True', 'False', 'False'],
        'Earthquake': ['True', 'False', 'True', 'False'],
        'P(Alarm=T)': [0.94, 0.95, 0.31, 0.001]
    }
    df_alarm = pd.DataFrame(alarm_data)
    st.table(df_alarm)
    
    # Calculation Example
    st.markdown("### 🧮 Example Calculation")
    
    st.markdown('<div class="formula-box"><p><strong>Find:</strong> P(Alarm=T, David=T, Sophia=T, ¬Burglary, ¬Earthquake)</p></div>', unsafe_allow_html=True)
    
    st.latex(r"= P(S|A) \times P(D|A) \times P(A|\neg B, \neg E) \times P(\neg B) \times P(\neg E)")
    st.latex(r"= 0.75 \times 0.91 \times 0.001 \times 0.998 \times 0.999 = 0.00068")
    
    st.success("**Very low probability!** Makes sense - alarm rarely goes off without burglary or earthquake.")

def render_certainty_factors():
    st.markdown('<p class="main-header">🔟 Certainty Factors</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="concept-box"><h3>🎯 What are Certainty Factors?</h3><p>A <strong>simpler alternative</strong> to full Bayesian probability. Uses a single number from -1 to +1 to express belief/disbelief.</p></div>', unsafe_allow_html=True)
    
    # Formula
    st.markdown("### 📐 The Formula")
    
    st.latex(r"CF[h,e] = MB[h,e] - MD[h,e]")
    
    st.markdown("""
    **Where:**
    - **MB** = Measure of Belief (0 to 1)
    - **MD** = Measure of Disbelief (0 to 1)
    - **CF** = Certainty Factor (-1 to +1)
    """)
    
    # Scale
    st.markdown("### 📊 CF Scale")
    
    st.markdown("""
    - **CF = +1** → Definitely true
    - **CF = +0.7** → Strong evidence for
    - **CF = 0** → No evidence either way
    - **CF = -0.7** → Strong evidence against
    - **CF = -1** → Definitely false
    """)
    
    # Example Rule
    st.markdown('<div class="example-box"><h4>🏥 Medical Rule Example</h4><p><strong>Rule:</strong></p><code>IF has-spots(X) AND has-fever(X)<br>THEN has-measles(X) CF = 0.5</code><p><strong>Meaning:</strong> Spots + fever gives moderate evidence (CF=0.5) for measles.</p></div>', unsafe_allow_html=True)
    
    # Combining Evidence
    st.markdown("### 🔗 Combining Evidence")
    
    st.latex(r"MB_{\text{combined}} = MB_1 + MB_2 \times (1-MB_1)")
    
    st.markdown('<div class="example-box"><p><strong>Example:</strong></p><ul><li>Evidence 1: MB=0.3 → CF=0.3</li><li>Evidence 2: MB=0.2</li></ul></div>', unsafe_allow_html=True)
    
    st.latex(r"MB_{\text{combined}} = 0.3 + 0.2 \times (1-0.3) = 0.44")
    
    st.success("**Combined CF = 0.44** (stronger than either alone!)")

def render_dempster_shafer():
    st.markdown('<p class="main-header">1️⃣1️⃣ Dempster-Shafer Theory</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="concept-box"><h3>🎯 What is Dempster-Shafer?</h3><p>An <strong>evidence theory</strong> that can represent <strong>ignorance</strong> explicitly and combine evidence from multiple sources.</p></div>', unsafe_allow_html=True)
    
    # Why DST
    st.markdown("### 🤔 Why Was It Developed?")
    
    prob_col, dst_col = st.columns(2)
    
    with prob_col:
        st.markdown('<div class="warning-box"><h4>Bayesian Problems</h4><ul><li>One evidence at a time</li><li>Can\'t represent "I don\'t know"</li><li>Probabilities must sum to 1</li></ul></div>', unsafe_allow_html=True)
    
    with dst_col:
        st.markdown('<div class="definition-box"><h4>DST Solutions</h4><ul><li>Combines multiple evidence</li><li>Explicitly shows ignorance</li><li>Uses intervals [Bel, Pl]</li></ul></div>', unsafe_allow_html=True)
    
    # Core Concepts
    st.markdown("### 📊 Core Concepts")
    
    st.markdown('<div class="formula-box"><p><strong>Belief (Bel):</strong> Minimum support (how sure we are)</p><p><strong>Plausibility (Pl):</strong> Maximum support (how possible)</p><p><strong>Ignorance = Pl - Bel</strong></p></div>', unsafe_allow_html=True)
    
    # Example
    st.markdown('<div class="example-box"><h4>Example: Unknown Disease</h4><p><strong>Bayesian:</strong> Must assign P(Disease1)=0.5, P(Disease2)=0.5 even with no evidence!</p><p><strong>DST:</strong> Bel(Disease1)=0, Pl(Disease1)=1 → Shows we don\'t know!</p></div>', unsafe_allow_html=True)
    
    # Combination Rule
    st.markdown("### 🔗 Dempster's Combination Rule")
    
    st.latex(r"(m_1 \oplus m_2)(C) = \frac{\sum_{A \cap B = C} m_1(A) \times m_2(B)}{1 - K}")
    
    st.markdown("**Combines evidence from independent sources!**")
    
    st.success("**DST is more flexible than Bayesian - can say 'I don't know'!**")

def render_fuzzy_logic():
    st.markdown('<p class="main-header">1️⃣2️⃣ Fuzzy Logic</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="definition-box"><h3>🎯 What is Fuzzy Logic?</h3><p>Allows <strong>partial truth</strong> - values between 0 and 1. Not just TRUE or FALSE!</p></div>', unsafe_allow_html=True)
    
    # Comparison
    st.markdown("### 🔄 Crisp vs Fuzzy")
    
    crisp_col, fuzzy_col = st.columns(2)
    
    with crisp_col:
        st.markdown('<div class="warning-box"><h4>Crisp Logic</h4><ul><li>Only 0 or 1</li><li>True or False</li><li>Sharp boundaries</li><li>Age > 60 = Old</li></ul></div>', unsafe_allow_html=True)
    
    with fuzzy_col:
        st.markdown('<div class="definition-box"><h4>Fuzzy Logic</h4><ul><li>0 to 1 (any value)</li><li>Partial truth</li><li>Smooth transitions</li><li>Age 55 = Old(0.6)</li></ul></div>', unsafe_allow_html=True)
    
    # Age Example
    st.markdown("### 👴 Age Membership Example")
    
    age_data = {
        'Age': [2, 10, 21, 30, 45, 70],
        'Infant': [1.0, 0, 0, 0, 0, 0],
        'Child': [0, 1.0, 0, 0, 0, 0],
        'Young': [0, 1.0, 1.0, 0.2, 0, 0],
        'Adult': [0, 0, 0.4, 1.0, 0.8, 0],
        'Old': [0, 0, 0, 0, 0.3, 1.0]
    }
    df_age = pd.DataFrame(age_data)
    st.table(df_age)
    
    st.info("**Notice:** Age 45 is Adult(0.8) AND Old(0.3). These don't sum to 1!")
    
    # Operations
    st.markdown("### 🔧 Fuzzy Operations")
    
    op1, op2, op3 = st.tabs(["Union", "Intersection", "Complement"])
    
    with op1:
        st.markdown("### Union (OR)")
        st.latex(r"\mu_{A \cup B}(x) = \max(\mu_A(x), \mu_B(x))")
        st.success("**Take the MAXIMUM!**")
    
    with op2:
        st.markdown("### Intersection (AND)")
        st.latex(r"\mu_{A \cap B}(x) = \min(\mu_A(x), \mu_B(x))")
        st.success("**Take the MINIMUM!**")
    
    with op3:
        st.markdown("### Complement (NOT)")
        st.latex(r"\mu_{A^c}(x) = 1 - \mu_A(x)")
        st.success("**1 minus membership!**")
    
    # Applications
    st.markdown("### 🚀 Applications")
    
    app_col1, app_col2, app_col3 = st.columns(3)
    
    with app_col1:
        st.markdown("""
        **Home:**
        - 🌡️ AC control
        - 🧺 Washing machines
        - 📺 Cameras
        """)
    
    with app_col2:
        st.markdown("""
        **Industry:**
        - 🏭 Process control
        - 🚂 Train speed
        - ✈️ Aircraft systems
        """)
    
    with app_col3:
        st.markdown("""
        **Other:**
        - 🏥 Medical diagnosis
        - 🎮 Game AI
        - 🎯 Pattern recognition
        """)
    
    st.success("**Fuzzy Logic = Human-like reasoning with partial truths!**")

# Main routing
if selected_topic == "🏠 Home":
    render_home()
elif selected_topic == "1️⃣ Uncertainty Basics":
    render_uncertainty_basics()
elif selected_topic == "2️⃣ Non-Monotonic Reasoning":
    render_non_monotonic()
elif selected_topic == "3️⃣ Truth Maintenance Systems":
    render_tms_overview()
elif selected_topic == "4️⃣ JTMS - Justification-Based TMS":
    render_jtms()
elif selected_topic == "5️⃣ LTMS - Logic-Based TMS":
    render_ltms()
elif selected_topic == "6️⃣ ATMS - Assumption-Based TMS":
    render_atms()
elif selected_topic == "7️⃣ Probabilistic Reasoning":
    render_probabilistic()
elif selected_topic == "8️⃣ Bayes' Theorem":
    render_bayes()
elif selected_topic == "9️⃣ Bayesian Networks":
    render_bayesian_networks()
elif selected_topic == "🔟 Certainty Factors":
    render_certainty_factors()
elif selected_topic == "1️⃣1️⃣ Dempster-Shafer Theory":
    render_dempster_shafer()
elif selected_topic == "1️⃣2️⃣ Fuzzy Logic":
    render_fuzzy_logic()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>🧠 AI Uncertainty & Reasoning Study Guide</strong></p>
    <p>Complete coverage of AI-3 PPT | Simple explanations | Real examples</p>
    <p>📚 Study efficiently | 💡 Master AI reasoning | 🎯 No fluff, just learning</p>
</div>
""", unsafe_allow_html=True)

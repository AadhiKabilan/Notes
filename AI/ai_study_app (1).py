import streamlit as st
import pandas as pd
from enum import Enum

# Set page config
st.set_page_config(page_title="AI Planning & Learning Study Guide", layout="wide")

# Custom CSS for better styling
st.markdown("""
<style>
    .concept-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
    }
    .example-box {
        background: #e8f4f8;
        padding: 15px;
        border-left: 5px solid #0288d1;
        border-radius: 5px;
        margin: 10px 0;
    }
    .definition-box {
        background: #fff3e0;
        padding: 15px;
        border-left: 5px solid #f57c00;
        border-radius: 5px;
        margin: 10px 0;
    }
    .warning-box {
        background: #ffebee;
        padding: 15px;
        border-left: 5px solid #c62828;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 AI Planning & Learning - Complete Study Guide")
st.markdown("---")

# Sidebar Navigation
st.sidebar.title("📚 Navigation")
chapters = [
    "Home",
    "1. Planning Fundamentals",
    "2. STRIPS & ADL",
    "3. State-Space Search",
    "4. Backward Search (Regression)",
    "5. Goal Stack Planning",
    "6. Partial Order Planning (POP)",
    "7. Non-Deterministic Planning",
    "8. Multi-Agent Planning",
    "9. Learning Concepts"
]

selected_chapter = st.sidebar.radio("Choose a topic:", chapters)

# ==================== HOME PAGE ====================
if selected_chapter == "Home":
    st.markdown("""
    # 📖 Welcome to AI Planning & Learning Study Guide
    
    This comprehensive guide covers:
    
    ### 🎯 Topics Covered:
    1. **Planning Fundamentals** - Understanding what planning is and classical planning environments
    2. **STRIPS & ADL** - Languages for representing planning problems
    3. **State-Space Search** - Forward and backward approaches to planning
    4. **Goal Stack Planning** - STRIPS method for solving conjunctive goals
    5. **Partial Order Planning** - POP technique for flexible plan generation
    6. **Non-Deterministic Planning** - Handling uncertainty in planning
    7. **Multi-Agent Planning** - Coordination between multiple agents
    8. **Learning Concepts** - Explanation-based and inductive learning
    
    ---
    
    ### 💡 How to Use This Guide:
    - Select a topic from the left sidebar
    - Read clear explanations with real-world examples
    - Understand complex concepts step-by-step
    - Visual diagrams and comparisons help you learn faster
    
    **Start learning by selecting a topic! →**
    """)

# ==================== CHAPTER 1: PLANNING FUNDAMENTALS ====================
elif selected_chapter == "1. Planning Fundamentals":
    st.header("🎯 Planning Fundamentals")
    
    st.markdown("""
    ## What is Planning?
    """)
    
    st.markdown("""
    <div class="definition-box">
    <b>Planning</b> is the task of coming up with a sequence of actions that will achieve a goal.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🌍 Classical Planning Environment")
    st.markdown("""
    Classical planning works in environments with these characteristics:
    """)
    
    # Table of properties
    properties = {
        "Property": [
            "Fully Observable",
            "Deterministic",
            "Finite",
            "Static",
            "Discrete"
        ],
        "What it means": [
            "Agent can see the complete state of the world",
            "Actions have predictable, certain outcomes",
            "Limited number of states and actions",
            "Environment doesn't change unless agent acts",
            "Clear, distinct states (not continuous)"
        ],
        "Example": [
            "We know exact position of blocks",
            "Moving a block always goes to intended location",
            "Fixed number of blocks, locations",
            "Blocks stay where we leave them",
            "Block is either ON or NOT ON another block"
        ]
    }
    
    df = pd.DataFrame(properties)
    st.dataframe(df, use_container_width=True)
    
    st.subheader("📝 Real-World Example: Umbrella Problem")
    st.markdown("""
    <div class="example-box">
    
    **Scenario:** You're at home in the rain and need to go to school. You have an umbrella.
    
    **Initial State:**
    - At(Home)
    - IsAt(Umbrella, Home)
    - Dry
    
    **Goal State:**
    - At(School)
    - Dry
    
    **Plan:**
    1. Take the umbrella
    2. Walk with umbrella to school
    
    Without planning, you might forget the umbrella and get wet!
    
    </div>
    """, unsafe_allow_html=True)

# ==================== CHAPTER 2: STRIPS & ADL ====================
elif selected_chapter == "2. STRIPS & ADL":
    st.header("🛠️ STRIPS & ADL - Representation Languages")
    
    st.subheader("What is STRIPS?")
    st.markdown("""
    <div class="definition-box">
    <b>STRIPS</b> = Standard Research Institute Problem Solver
    
    It's a language for writing planning problems using:
    - **States**: Conjunction of positive literals (facts that are TRUE)
    - **Actions**: With preconditions and effects
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📌 STRIPS State Representation")
    st.markdown("""
    In STRIPS:
    - Only list facts that are TRUE
    - Everything NOT listed is assumed FALSE
    - Use conjunctions (AND) to combine facts
    """)
    
    st.markdown("""
    <div class="example-box">
    
    **Example State:**
    ```
    At(Home) ∧ IsAt(Umbrella, Home) ∧ CanBeCarried(Umbrella) ∧ IsUmbrella(Umbrella) ∧ HandEmpty ∧ Dry
    ```
    
    This means:
    - ✓ I am at home
    - ✓ Umbrella is at home
    - ✓ Umbrella can be carried
    - ✓ Hand is empty
    - ✓ I am dry
    
    Everything else = FALSE (e.g., NOT(AtSchool), NOT(Holding(Book)))
    
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔧 STRIPS Action Representation")
    st.markdown("""
    Each action has three parts:
    1. **Action Name & Parameters**
    2. **Preconditions**: What must be true to execute the action
    3. **Effects**: What becomes true/false after the action
    """)
    
    st.markdown("""
    <div class="example-box">
    
    **Action: TakeObject(location, x)**
    
    **Preconditions (must be TRUE):**
    - HandEmpty
    - CanBeCarried(x)
    - At(location)
    - IsAt(x, location)
    
    **Effects (what changes):**
    - Add: Holding(x)
    - Remove: HandEmpty
    - Remove: IsAt(x, location)
    
    **In plain English:**
    "To pick up an object, your hand must be empty, you must be at that location, and the object must be there."
    
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Example Action 1: Walk with Umbrella")
        st.markdown("""
        ```
        WalkWithUmbrella(location1, location2, umbr)
        
        Preconditions:
        - At(location1)
        - Holding(umbr)
        - IsUmbrella(umbr)
        
        Effects:
        + At(location2)
        - At(location1)
        ```
        """)
    
    with col2:
        st.subheader("Example Action 2: Walk WITHOUT Umbrella")
        st.markdown("""
        ```
        WalkWithoutUmbrella(location1, location2)
        
        Preconditions:
        - At(location1)
        
        Effects:
        + At(location2)
        - At(location1)
        - Dry  ← You get wet!
        ```
        """)
    
    st.divider()
    
    st.subheader("ADL (Action Description Language)")
    st.markdown("""
    <div class="definition-box">
    <b>ADL</b> is more expressive than STRIPS. It allows:
    - Conditional effects
    - Universal quantification
    - Negative preconditions
    - More flexible variable typing
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
    
    **Comparison: STRIPS vs ADL**
    
    **STRIPS:**
    ```
    Action: Fly(P, from, to)
    Preconditions: At(P, from) ∧ Plane(P) ∧ Airport(from) ∧ Airport(to)
    Effects: ¬At(P, from) ∧ At(P, to)
    ```
    
    **ADL (more detailed):**
    ```
    Action: Fly(P: Plane, from: Airport, to: Airport)
    Preconditions: At(P, from) ∧ Airport(from) ∧ Airport(to)
    Effects: ¬At(P, from) ∧ At(P, to)
    (Note: Type constraints in parameters themselves)
    ```
    
    </div>
    """, unsafe_allow_html=True)

# ==================== CHAPTER 3: STATE-SPACE SEARCH ====================
elif selected_chapter == "3. State-Space Search":
    st.header("🔍 State-Space Search Methods")
    
    st.markdown("""
    There are **two main directions** to search for a plan:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1️⃣ Forward Search (Progression)")
        st.markdown("""
        <div class="concept-box">
        Start from INITIAL STATE → Search towards GOAL
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **How it works:**
        1. Begin at the starting state
        2. Apply all applicable actions
        3. Generate all successor states
        4. Continue until goal is reached
        
        **Like:** Planning a trip from home to destination
        """)
    
    with col2:
        st.subheader("2️⃣ Backward Search (Regression)")
        st.markdown("""
        <div class="concept-box">
        Start from GOAL → Search towards INITIAL STATE
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **How it works:**
        1. Begin at the goal state
        2. Find actions that achieve the goal
        3. Generate predecessor states
        4. Continue until initial state is satisfied
        
        **Like:** Planning a trip from destination backwards
        """)
    
    st.divider()
    
    st.subheader("⚠️ Problem with Forward Search: HUGE Branching Factor!")
    
    st.markdown("""
    <div class="warning-box">
    
    **Air Cargo Problem Example:**
    - 10 airports, each with 5 planes and 20 cargo pieces
    - 50 planes can each fly to 9 other airports: **50 × 9 = 450 actions**
    - 200 cargo pieces can be loaded/unloaded: **200+ more actions**
    - **Total ≈ 1000+ possible actions at each state!**
    
    This creates a HUGE search tree that's very inefficient.
    
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("✅ Why Backward Search is Better")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Forward Search (Bad)**")
        st.markdown("""
        - Considers ALL applicable actions
        - Many irrelevant actions explored
        - Huge branching factor (~1000)
        - Wastes time on wrong paths
        """)
    
    with col2:
        st.markdown("**Backward Search (Good)**")
        st.markdown("""
        - Only considers RELEVANT actions
        - Action is relevant if it achieves a goal
        - Small branching factor (~20)
        - More efficient problem solving
        """)
    
    st.divider()
    
    st.subheader("📊 Practical Comparison")
    
    st.markdown("""
    <div class="example-box">
    
    **Goal:** Move 20 cargo pieces from Airport A to Airport B
    
    **Forward Search:**
    - Which 1000 actions to try? Pick any!
    - Most don't help with the goal
    - Explores massive search space
    
    **Backward Search:**
    - Goal: At(Cargo1, B) ∧ At(Cargo2, B) ∧ ... ∧ At(Cargo20, B)
    - Only relevant action: **Unload(Cargo1, plane, B)**
    - This narrows down the search significantly
    - Much faster!
    
    </div>
    """, unsafe_allow_html=True)

# ==================== CHAPTER 4: BACKWARD SEARCH (REGRESSION) ====================
elif selected_chapter == "4. Backward Search (Regression)":
    st.header("↩️ Backward Search & Regression Planning")
    
    st.markdown("""
    <div class="definition-box">
    <b>Regression Planning</b> is backward search where we ask:
    "What states must be true BEFORE this action to reach the goal?"
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🎯 Key Concept: Relevant Actions")
    
    st.markdown("""
    <div class="example-box">
    
    **Definition:** An action is RELEVANT to a goal if it **achieves one of the goal's conjuncts**.
    
    **Example:**
    - Goal: At(C1, B) ∧ At(C2, B) ∧ ... ∧ At(C20, B)
    - Relevant action: **Unload(C1, plane, B)** ✓ (achieves first conjunct)
    - Irrelevant action: Fly(EmptyPlane, A, C) ✗ (doesn't achieve any goal)
    
    By focusing on relevant actions, we explore MUCH fewer options!
    
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔄 How Regression Works")
    
    st.markdown("""
    When we regress a goal through an action, we ask:
    **"What must be true BEFORE this action to satisfy the goal AFTER?"**
    """)
    
    st.markdown("""
    <div class="example-box">
    
    **Step 1: Start with goal**
    ```
    Goal: At(C1, B) ∧ At(C2, B) ∧ At(C3, B)
    ```
    
    **Step 2: Choose relevant action**
    ```
    Action: Unload(C1, plane, B)
    
    Preconditions: In(C1, plane) ∧ At(plane, B)
    Effects: At(C1, B) ∧ ¬In(C1, plane)
    ```
    
    **Step 3: Regress the goal**
    
    To satisfy the original goal with this action:
    - Add the action's preconditions to the new goal
    - Remove the goal conjuncts achieved by this action
    
    ```
    New Goal = 
      In(C1, plane) ∧ At(plane, B)           ← from preconditions
      ∧ At(C2, B) ∧ At(C3, B)                ← still need these
    ```
    
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("⚖️ Two Constraints for Valid Regression")
    
    st.markdown("""
    1. **Relevant**: Action achieves a goal conjunct ✓
    2. **Consistent**: Action doesn't undo other goal conjuncts ✓
    """)
    
    st.markdown("""
    <div class="warning-box">
    
    **Bad Action Example:**
    If we try action Load(C2, plane) when C2 is supposed to be at B:
    - This would make At(C2, B) false!
    - It's NOT consistent with the goal
    - So we DON'T use it
    
    </div>
    """, unsafe_allow_html=True)

# ==================== CHAPTER 5: GOAL STACK PLANNING ====================
elif selected_chapter == "5. Goal Stack Planning":
    st.header("📚 Goal Stack Planning (STRIPS Method)")
    
    st.markdown("""
    <div class="definition-box">
    <b>Goal Stack Planning</b> is the first method used to solve problems with interacting goals.
    
    It uses a single STACK containing both GOALS and OPERATORS to achieve them.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🧱 Classic Example: Blocks World")
    
    st.markdown("""
    <div class="example-box">
    
    **Initial State:**
    ```
    A is on table
    B is on A
    C is on table
    D is on table
    ```
    
    **Goal:**
    ```
    C on top of A
    B on top of D
    A on table
    D on table
    ```
    
    **Visual:**
    ```
    Initial:          Goal:
      B                 C
      A  C  D           A  B  D
    [TABLE]         [TABLE]
    ```
    
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔧 How Goal Stack Planning Works")
    
    st.markdown("""
    1. **Start** with the goal on the stack
    2. **Pop** the top goal from stack
    3. **Check** if it's already true - if yes, continue
    4. **Find** an operator that achieves this goal
    5. **Add** operator AND its preconditions to stack
    6. **Repeat** until stack is empty
    7. **Execute** operators in the order they were popped
    """)
    
    st.markdown("""
    <div class="example-box">
    
    **Step-by-step for Blocks World:**
    
    **Stack Initially:**
    ```
    ON(C, A)
    ON(B, D)
    ONTABLE(A)
    ONTABLE(D)
    ```
    
    **Processing ON(C, A):**
    - It's not true, need STACK(C, A) operator
    - STACK(C, A) needs: CLEAR(A) ∧ HOLDING(C)
    - Add these as sub-goals
    
    **Heuristic:** If HOLDING is one of several goals, do it LAST!
    (Because picking something up makes hand full)
    
    **New Stack:**
    ```
    CLEAR(A)          ← do first
    HOLDING(C)        ← do last
    STACK(C, A)       ← the operator
    ON(B, D)          ← remaining goals
    ```
    
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("⚡ Key Insight: Heuristic Ordering")
    
    st.markdown("""
    <div class="concept-box">
    Some goals should be achieved in a specific order to avoid conflicts!
    
    **Example:** If you need HOLDING(C) and CLEAR(A):
    - Do CLEAR(A) first (doesn't require arm)
    - Do HOLDING(C) last (uses the arm)
    
    This avoids having to pick up C twice!
    </div>
    """, unsafe_allow_html=True)

# ==================== CHAPTER 6: PARTIAL ORDER PLANNING ====================
elif selected_chapter == "6. Partial Order Planning (POP)":
    st.header("🎯 Partial Order Planning (POP)")
    
    st.markdown("""
    <div class="definition-box">
    <b>POP</b> is a planning method that doesn't require a fixed order of actions.
    
    Instead of linear plans → flexible plans with only necessary orderings
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Why POP is Better Than Linear Planning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Linear Planning**")
        st.markdown("""
        - Actions in fixed order: A→B→C
        - If A and C are independent, 
          still must order them
        - Less flexible
        """)
    
    with col2:
        st.markdown("**Partial Order Planning**")
        st.markdown("""
        - Actions in flexible order
        - Only constrain what's necessary
        - A can happen anytime before C
        - More efficient
        """)
    
    st.divider()
    
    st.subheader("📋 Components of a Partial Plan")
    
    st.markdown("""
    1. **Actions**: The steps in the plan
    2. **Ordering Constraints**: Which actions must happen before others
    3. **Causal Links**: Why one action is needed for another
    4. **Open Preconditions**: Goals still needing to be satisfied
    """)
    
    st.markdown("""
    <div class="example-box">
    
    **Simple Example: Getting Dressed**
    
    **Actions:**
    - Put on right sock
    - Put on right shoe
    - Put on left sock
    - Put on left shoe
    
    **Necessary Ordering Constraints:**
    - Right sock BEFORE right shoe
    - Left sock BEFORE left shoe
    - (But right side can happen in any order with left side!)
    
    **NOT necessary:**
    - Right sock before left sock (they're independent)
    
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔗 Causal Links (Protection Intervals)")
    
    st.markdown("""
    <div class="example-box">
    
    **Notation:** A →ₚ B reads as "A achieves proposition p for B"
    
    **Example:**
    ```
    RightSock →RightSockOn RightShoe
    
    This means:
    - RightSock action makes RightSockOn true
    - RightShoe needs RightSockOn to be true
    - RightSockOn must stay true from RightSock to RightShoe
    ```
    
    **Protection Interval:** The time period where p must remain true
    
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("⚠️ Handling Threats to Causal Links")
    
    st.markdown("""
    A **threat** occurs when an action might make a protected proposition false.
    
    **Solutions:**
    1. **Demotion**: Place the threatening action BEFORE the protected link
    2. **Promotion**: Place the threatening action AFTER the protected link
    """)
    
    st.markdown("""
    <div class="example-box">
    
    **Example: Putting on shoes and socks**
    
    **Causal Link:** Socks →Dry RightShoe
    (Putting on socks makes feet dry for putting on shoe)
    
    **Threat:** Jumping in water action would make Dry false!
    
    **Solution:**
    - **Demotion**: Do jump-in-water BEFORE putting on socks
    - **Promotion**: Do jump-in-water AFTER putting on shoe
    
    Either way, the causal link is protected!
    
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🏗️ Building a Partial Plan")
    
    st.markdown("""
    **Step 1: Start with dummy actions**
    ```
    Start: No preconditions, effects are initial state
    Finish: Preconditions are goals, no effects
    ```
    
    **Step 2: Identify open preconditions**
    - These are goals not yet satisfied
    
    **Step 3: For each open precondition**
    - Find an action that achieves it
    - Add causal link
    - Add action to plan
    
    **Step 4: Handle conflicts**
    - Resolve threats through demotion/promotion
    - Add ordering constraints
    
    **Step 5: Repeat until no open preconditions**
    """)

# ==================== CHAPTER 7: NON-DETERMINISTIC PLANNING ====================
elif selected_chapter == "7. Non-Deterministic Planning":
    st.header("🌊 Planning Under Uncertainty")
    
    st.markdown("""
    Real world is NOT like classical planning!
    - Outcomes are uncertain
    - Partial observability (can't see everything)
    - Dynamic (things change unexpectedly)
    """)
    
    st.subheader("4️⃣ Approaches to Uncertain Planning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**1. Sensorless Planning**")
        st.markdown("""
        Also called: **Conformant Planning**
        
        Execute one plan for ALL possible situations
        
        **Example:**
        - Paint chair and table same color without looking
        - Just paint both colors blindly
        """)
        
        st.markdown("**2. Conditional Planning**")
        st.markdown("""
        Also called: **Contingency Planning**
        
        Plan differently based on what you sense
        
        **Example:**
        ```
        if airport_operational:
            fly_there()
        else:
            fly_alternate()
        ```
        """)
    
    with col2:
        st.markdown("**3. Execution Monitoring**")
        st.markdown("""
        Execute plan & monitor if it's working
        
        Replan if something goes wrong
        
        **Example:**
        - Try to paint furniture
        - If spots missed, repaint them
        """)
        
        st.markdown("**4. Continuous Planning**")
        st.markdown("""
        Plan & execute together continuously
        
        Adapt to new situations as they arise
        
        **Example:**
        - Going out for dinner, but if sick, postpone
        - Reactive to environment changes
        """)
    
    st.divider()
    
    st.subheader("🔍 Conditional Planning Example: Vacuum World")
    
    st.markdown("""
    <div class="example-box">
    
    **Environment:** Robot in house with dirty and clean squares
    
    **Actions:**
    - Left, Right (move)
    - Suck (clean current square)
    
    **Problem:** Robot doesn't always know if squares are dirty
    
    **Solution - Conditional Plan:**
    ```
    if AtLeft AND CleanLeft:
        Go Right
    else:
        Suck
    ```
    
    This handles multiple possible states!
    
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🎓 Partially Observable Environments")
    
    st.markdown("""
    Agent has **belief state** (what it thinks is true):
    - Start with set of possible initial states
    - Update beliefs based on sensing
    """)
    
    st.markdown("""
    <div class="example-box">
    
    **Example: Vacuum World**
    
    **What robot knows:**
    - At(Right) ∧ Clean(Right)
    
    **What robot doesn't know:**
    - Is Left square clean? Could be either:
      - {(AtR ∧ CleanR ∧ CleanL), (AtR ∧ CleanR ∧ ¬CleanL)}
    
    **Sensing Options:**
    1. **Automatic sensing**: Get all facts each step
    2. **Active sensing**: Execute sensing actions (CheckDirt)
    
    </div>
    """, unsafe_allow_html=True)

# ==================== CHAPTER 8: MULTI-AGENT PLANNING ====================
elif selected_chapter == "8. Multi-Agent Planning":
    st.header("👥 Planning with Multiple Agents")
    
    st.markdown("""
    <div class="definition-box">
    When multiple agents must work together, they need to coordinate!
    
    **Cooperative environment**: Agents have shared goals and joint plans
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🎯 Multi-Agent Planning Basics")
    
    st.markdown("""
    - **Multiple agents**: A, B, C, etc.
    - **Joint goals**: Shared objectives
    - **Communication**: Agents must coordinate
    - **Joint plan**: Sequence of actions for each agent
    """)
    
    st.subheader("🏏 Example: Cricket Batting")
    
    st.markdown("""
    <div class="example-box">
    
    **Agents:** Batsman(A) and Fielder(B)
    
    **Scenario:** Need to hit ball to score runs
    
    **Plan Option 1:**
    ```
    Agent A: Go to right baseline → Hit ball
    Agent B: No operation (standby)
    ```
    Result: A hits, B doesn't interfere → SUCCESS ✓
    
    **Plan Option 2:**
    ```
    Agent A: Go to left net → No operation
    Agent B: Go to right baseline → Hit ball
    ```
    Result: B hits, A doesn't interfere → SUCCESS ✓
    
    **CONFLICT - If A chooses Plan 1 but B chooses Plan 2:**
    ```
    A tries to hit, B also tries to hit
    → INTERFERENCE, FAILURE ✗
    ```
    
    **Solution:** Agents must AGREE on which plan to execute!
    
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🤝 Coordination Mechanisms")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Communication**")
        st.markdown("""
        - Agents discuss plans
        - Agree on roles
        - Share information
        """)
    
    with col2:
        st.markdown("**Co-operation**")
        st.markdown("""
        - Joint goal commitment
        - Synchronized execution
        - Mutual support
        """)
    
    st.markdown("""
    <div class="warning-box">
    
    **Key Challenge:** Without coordination, agents might:
    - Execute conflicting plans
    - Waste resources
    - Fail to achieve goals
    
    </div>
    """, unsafe_allow_html=True)

# ==================== CHAPTER 9: LEARNING ====================
elif selected_chapter == "9. Learning Concepts":
    st.header("🧠 Learning in AI")
    
    st.markdown("""
    There are two main types of learning:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1️⃣ Explanation-Based Learning (EBL)")
        st.markdown("""
        Learn from examples using existing knowledge
        
        **Process:**
        1. Have domain theory (background knowledge)
        2. Given training example
        3. Explain why example is true
        4. Generalize the explanation
        5. Add generalized rule to knowledge
        """)
    
    with col2:
        st.subheader("2️⃣ Inductive Learning")
        st.markdown("""
        Learn patterns from many examples
        
        **Process:**
        1. Observe multiple examples
        2. Find patterns
        3. Create general rules
        4. Test on new data
        
        "Bottom-up" approach
        """)
    
    st.divider()
    
    st.subheader("📚 Explanation-Based Learning Example: What's a Cup?")
    
    st.markdown("""
    <div class="example-box">
    
    **Domain Theory (what we know):**
    ```
    cup(X) :- liftable(X) ∧ holds_liquid(X)
    
    holds_liquid(Z) :- part(Z,W) ∧ concave(W) ∧ points_up(W)
    
    liftable(X) :- light(X) ∧ has_handle(X)
    
    light(X) :- small(X)
    ```
    
    **Training Example: obj1 is a cup**
    ```
    Properties of obj1:
    - small(obj1)           ← makes it light
    - part(obj1, handle)    ← has handle
    - part(obj1, bowl)      ← has bowl part
    - concave(bowl)         ← bowl is concave
    - points_up(bowl)       ← bowl points up
    - color(obj1, red)      ← RED (irrelevant!)
    ```
    
    **Step 1: Prove obj1 is a cup**
    Using domain theory:
    - small(obj1) → light(obj1) → liftable(obj1) ✓
    - bowl properties → holds_liquid(obj1) ✓
    - Therefore: cup(obj1) ✓
    
    **Step 2: Generalize the proof**
    Replace constants with variables:
    ```
    cup(X) :- small(X) ∧
              part(X, handle) ∧
              part(X, W) ∧
              concave(W) ∧
              points_up(W)
    ```
    
    **Step 3: Add to knowledge base**
    Now we have a new rule for identifying cups!
    
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔍 Why EBL is Powerful")
    
    st.markdown("""
    ✓ **Accurate**: Based on proven domain theory
    
    ✓ **Relevant**: Only relevant facts included
    
    ✓ **Efficient**: Pre-computed knowledge
    
    ✗ Not good with limited domain theory
    """)
    
    st.divider()
    
    st.subheader("📊 Inductive Learning")
    
    st.markdown("""
    <div class="example-box">
    
    **Approach:** "Learn by observing"
    
    **Example: Recognizing fruit**
    - See 100 apples: red, round, small
    - See 100 oranges: orange, round, medium
    - Create rule: IF red AND small THEN apple
    
    **Advantages:**
    - Works without domain theory
    - Discovers patterns automatically
    - Good for new domains
    
    **Challenges:**
    - Need many examples
    - May overfit to training data
    - Hard to verify correctness
    
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("💡 Inductive vs Deductive Learning")
    
    comparison_data = {
        "Aspect": ["Direction", "Starting Point", "Method", "Examples Needed", "Certainty", "Best For"],
        "Inductive": ["Bottom-up", "Specific examples", "Find patterns", "Many (50+)", "Probabilistic", "Unknown domains"],
        "Deductive": ["Top-down", "General theory", "Apply rules", "Few (1-5)", "Certain", "Known domains"]
    }
    
    st.dataframe(pd.DataFrame(comparison_data), use_container_width=True)

# Footer
st.divider()
st.markdown("""
---
**Study Tips:**
- 📖 Read each section carefully
- ✏️ Take notes on key concepts
- 🧠 Try to explain to a friend
- 💻 Implement examples in code
- 🎯 Focus on understanding, not memorizing

Happy Learning! 🚀
""")

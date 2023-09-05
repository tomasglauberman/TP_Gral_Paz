# Agent-based model simulation for travel times in Buenos Aires city
We developed an agent-based model simulation to understand the dynamics of the transport system and quantify the variations in travel time  under different policies in Buenos Aires city.

A typical agent-based model has three elements:

1. A set of *agents*, their attributes and behaviours.
2. A set of agent *relationships* and methods of interaction.
3. An *environment* in which agents interact (with the env and other agents).

## Initial model definition
 We aim to determine the distribution of travel time over a 12km segment of road and experiment how the distribution changes with different rules for the environment, such as speed limits and weather conditions.
 

### Agents
Agents are cars in our model (or people driving cars).   
  
*Static attributes:*
- **Prefered-speed**: the speed at which the agent prefers to travel.
- **Mistake-p**: the probability of making a mistake at any given time. The higher the value, the higher the risk of accident. (There should be some more complex relationship between the probabilty of having an accident, Mistake-p and Prefered-speed) 
- **Reaction-time**: time it takes for an agent to respond. This value must be around the same for all agents (or it might change based on visibility or capacity of each agent).  

*Dynamic attributes:* 
- **Position**: a vector for the current position in space.
- **Velocity**: a vector for the current velocity.
- **Acceleration**: a vector for the current acceleration. This attribute can take positive and negative values.
- **Active**: indicator of agent actively traveling or already at destination.   

Agents move from starting point in Avenida General Paz and travel 12km to destination point. On our first model, the environment is a single straight road, but it could be improved to more realistic conditions such as a multiple lanes road or an addition of curves.

Agents have to drive from one point to another under the following basic behaviour. It is important to note that the agent only controls the **Acceleration** attribute, deciding if gaining speed (Acc > 0), keeping speed constant(Acc = 0) or decelerating (Acc < 0). The rules for each agent are:
1. Try to reach **Preferd-speed** while traveling (with some small shocks potentially). This is achieved by updating **Acceleration** in the following way:    

    $Acc_{t+1} = \alpha_{t+1}(\text{Pref-speed} - Vel_{t})$  
 
    where $\alpha_{t+1} = (-9.75*10^{-5})Vel_t^2 + (0.0117)Vel_t + 0.05$ is the **acceleration rate** (could be influenced by Reaction-time, car force, or a new attribute for each agent). TO DO: VER GRAFICOS DE ACELERACION BEHAVIOUR

2. Sense surroundings to check on neighbours with probability $(1- \text{Mistake-p})$. 

---

### Interactions

5. How do the agents interact with each other? With the
environment? How expansive or focused are agent
interactions?

6. Where might the data come from, especially on agent
behaviours, for such a model?

7. How might you validate the model, especially the agent
behaviours?

### Environment
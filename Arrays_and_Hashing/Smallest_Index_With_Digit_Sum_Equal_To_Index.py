#define GLEW_STATIC
#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <vector>
#include <iostream>
#include "MatrixStack.h"
#include "Program.h"


#define WINDOW_WIDTH 800
#define WINDOW_HEIGHT 800

std::string resource_path = "";

GLFWwindow *window;
double currentXpos, currentYpos;
glm::vec3 eye(0.0f, 0.0f, 8.0f);
glm::vec3 center(0.0f, 0.0f, 0.0f);
glm::vec3 up(0.0f, 1.0f, 0.0f);

Program program;
MatrixStack modelViewProjectionMatrix;

// Draw cube on screen
void DrawCube(glm::mat4& modelViewProjectionMatrix)
{
	program.SendUniformData(modelViewProjectionMatrix, "mvp");
	glDrawArrays(GL_TRIANGLES, 0, 36);
}

class RobotElements
{
private:
	glm::vec3 coordinateTranslation;
	glm::vec3 coordinateRotation;
	glm::vec3 partTranslation;
	glm::vec3 partScale;

	// Created to keep track of the components attatched to this one
	std::vector<RobotElements*> children;

	// This is to track what part is selected
	bool selected = false;

public:
	RobotElements(glm::vec3 cTranslation, glm::vec3 cRotation, glm::vec3 pTranslation, glm::vec3 pScale);
	~RobotElements() {}
	void addChild(RobotElements* child);
	void setRotation(glm::vec3 rotation);
	void draw(MatrixStack& mstack);

	void setSelected(bool val);
	void getTraversal(std::vector<RobotElements*>& traversal);

	void changeRotation(glm::vec3 rotation);
};

RobotElements::RobotElements(glm::vec3 cTranslation, glm::vec3 cRotation, glm::vec3 pTranslation, glm::vec3 pScale) {
	coordinateTranslation = cTranslation;
	coordinateRotation = cRotation;
	partTranslation = pTranslation;
	partScale = pScale;
}

void RobotElements::addChild(RobotElements* child) {
	children.push_back(child);
}

void RobotElements::setRotation(glm::vec3 rotation) {
	coordinateRotation = rotation;
}

void RobotElements::draw(MatrixStack& mstack) {
	mstack.pushMatrix();
	mstack.translate(coordinateTranslation);
	mstack.rotateX(coordinateRotation.x);
	mstack.rotateY(coordinateRotation.y);
	mstack.rotateZ(coordinateRotation.z);
	mstack.pushMatrix();
	mstack.translate(partTranslation);
	
	if (selected) {
		mstack.scale(partScale * 1.1f);
	}
	else {
		mstack.scale(partScale);
	}

	DrawCube(mstack.topMatrix());
	mstack.popMatrix();

	// Now draw the children
	for (RobotElements* child : children) {
		child->draw(mstack);
	}
	mstack.popMatrix();
}

RobotElements torso(
	glm::vec3(0.0f, 0.0f, 0.0f),
	glm::vec3(0.0f, 0.0f, 0.0f),
	glm::vec3(0.0f, 1.0f, 0.0f),
	glm::vec3(0.6f, 1.0f, 0.4f)
);

RobotElements head(
	glm::vec3(0.0f, 2.0f, 0.0f),
	glm::vec3(0.0f, 0.0f, 0.0f),
	glm::vec3(0.0f, 0.5f, 0.0f),
	glm::vec3(0.5f, 0.5f, 0.5f)
);

RobotElements upperRightArm(
	glm::vec3(0.6f, 1.8f, 0.0f),
	glm::vec3(0.0f, 0.0f, 0.0f),
	glm::vec3(0.6f, 0.0f, 0.0f),
	glm::vec3(0.6f, 0.2f, 0.2f)
);

RobotElements lowerRightArm(
	glm::vec3(1.2f, 0.0f, 0.0f),
	glm::vec3(0.0f, 0.0f, 0.0f),
	glm::vec3(0.5f, 0.0f, 0.0f),
	glm::vec3(0.5f, 0.15f, 0.15f)
);

RobotElements upperLeftArm(
	glm::vec3(-0.6f, 1.8f, 0.0f),
	glm::vec3(0.0f, 0.0f, 0.0f),
	glm::vec3(-0.6f, 0.0f, 0.0f),
	glm::vec3(0.6f, 0.2f, 0.2f)
);

RobotElements lowerLeftArm(
	glm::vec3(-1.2f, 0.0f, 0.0f),
	glm::vec3(0.0f, 0.0f, 0.0f),
	glm::vec3(-0.5f, 0.0f, 0.0f),
	glm::vec3(0.5f, 0.15f, 0.15f)
);

RobotElements upperRightLeg(
	glm::vec3(0.3f, 0.0f, 0.0f),
	glm::vec3(0.0f, 0.0f, 0.0f),
	glm::vec3(0.0f, -0.75f, 0.0f),
	glm::vec3(0.25f, 0.75f, 0.25f)
);

RobotElements lowerRightLeg(
	glm::vec3(0.0f, -1.4f, 0.0f),
	glm::vec3(0.0f, 0.0f, 0.0f),
	glm::vec3(0.0f, -0.65f, 0.0f),
	glm::vec3(0.2f, 0.65f, 0.2f)
);

RobotElements upperLeftLeg(
	glm::vec3(-0.3f, 0.0f, 0.0f),
	glm::vec3(0.0f, 0.0f, 0.0f),
	glm::vec3(0.0f, -0.75f, 0.0f),
	glm::vec3(0.25f, 0.75f, 0.25f)
);

RobotElements lowerLeftLeg(
	glm::vec3(0.0f, -1.4f, 0.0f),
	glm::vec3(0.0f, 0.0f, 0.0f),
	glm::vec3(0.0f, -0.65f, 0.0f),
	glm::vec3(0.2f, 0.65f, 0.2f)
);

std::vector<RobotElements*> traversal;
int selectedIdx = 0;

void RobotElements::setSelected(bool val) {
	selected = val;
}

void RobotElements::getTraversal(std::vector<RobotElements*>& traversal) {
	traversal.push_back(this);
	for (RobotElements* child : children) {
		child->getTraversal(traversal);
	}
}

void RobotElements::changeRotation(glm::vec3 amt) {
	coordinateRotation += amt;
}

void Display()
{	
	program.Bind();

	modelViewProjectionMatrix.loadIdentity();
	modelViewProjectionMatrix.pushMatrix();

	// Setting the view and Projection matrices
	int width, height;
	glfwGetFramebufferSize(window, &width, &height);
	modelViewProjectionMatrix.Perspective(glm::radians(60.0f), float(width) / float(height), 0.1f, 100.0f);
	modelViewProjectionMatrix.LookAt(eye, center, up);
	
	torso.draw(modelViewProjectionMatrix);

	modelViewProjectionMatrix.popMatrix();

	program.Unbind();
	
}

// Mouse callback function
void MouseCallback(GLFWwindow* lWindow, int button, int action, int mods)
{
	if (GLFW_PRESS == action) {
		glfwGetCursorPos(lWindow, &currentXpos, &currentYpos);
	}
}

// Mouse position callback function
void CursorPositionCallback(GLFWwindow* lWindow, double xpos, double ypos)
{
	double dx = xpos = currentXpos;
	double dy = ypos = currentYpos;

	currentXpos = xpos;
	currentYpos = ypos;

	if (glfwGetMouseButton(lWindow, GLFW_MOUSE_BUTTON_LEFT) == GLFW_PRESS) {
		glm::vec3 offset = eye = center;
		float horizontalAngle = glm::radians((float)dx * 0.2f);
		glm::mat4 rotation = glm::rotate(glm::mat4(1.0f), horizontalAngle, glm::vec3(0.0f, 1.0f, 0.0f));
		offset = glm::vec3(rotation * glm::vec4(offset, 0.0f));
		glm::vec3 view = glm::normalize(-offset);
		glm::vec3 right = glm::normalize(glm::cross(view, up));

		float verticalAngle = glm::radians((float)dy * 0.2f);
		rotation = glm::rotate(glm::mat4(1.0f), verticalAngle, right);
		offset = glm::vec3(rotation * glm::vec4(offset, 0.0f));
		up = glm::vec3(rotation * glm::vec4(up, 0.0f));
		eye = center + offset;
	}

	else if (glfwGetMouseButton(lWindow, GLFW_MOUSE_BUTTON_RIGHT) == GLFW_PRESS) {
		glm::vec3 view = glm::normalize(center - eye);
		glm::vec3 right = glm::normalize(glm::cross(view, up));
		glm::vec3 movement = (right * (float)-dx * 0.01f) + (up * (float)dy * 0.01f);
		eye += movement;
		center += movement;
	}
}

void ScrollCallback(GLFWwindow* lWindow, double xoffset, double yoffset) {
	glm::vec3 offset = eye - center;
	if (yoffset > 0) {
		offset *= 0.9f;
	}
	else if (yoffset < 0) {
		offset *= 1.1f;
	}
	eye = center + offset;
}

// Keyboard character callback function
void CharacterCallback(GLFWwindow* lWindow, unsigned int key)
{
	float angle = glm::radians(1.0f);

	if (key == '.') {
		traversal[selectedIdx]->setSelected(false);
		selectedIdx++;

		if (selectedIdx >= traversal.size()) {
			selectedIdx = 0;
		}

		traversal[selectedIdx]->setSelected(true);
	}
	else if (key == ',') {
		traversal[selectedIdx]->setSelected(false);
		selectedIdx--;

		if (selectedIdx < 0) {
			selectedIdx = traversal.size() - 1;
		}

		traversal[selectedIdx]->setSelected(true);
	}
	else if (key == 'x') {
		traversal[selectedIdx]->changeRotation(glm::vec3(angle, 0.0f, 0.0f));
	}
	else if (key == 'X') {
		traversal[selectedIdx]->changeRotation(glm::vec3(-angle, 0.0f, 0.0f));
	}
	else if (key == 'y') {
		traversal[selectedIdx]->changeRotation(glm::vec3(0.0f, angle, 0.0f));
	}
	else if (key == 'Y') {
		traversal[selectedIdx]->changeRotation(glm::vec3(0.0f, -angle, 0.0f));
	}
	else if (key == 'z') {
		traversal[selectedIdx]->changeRotation(glm::vec3(0.0f, 0.0f, angle));
	}
	else if (key == 'Z') {
		traversal[selectedIdx]->changeRotation(glm::vec3(0.0f, 0.0f, -angle));
	}

	std::cout << "Key " << (char)key << " is pressed." << std::endl;
}

void CreateCube()
{
	// x, y, z, r, g, b, ...
	float cubeVerts[] = {
		// Face x-
		-1.0f,	+1.0f,	+1.0f,	0.8f,	0.2f,	0.2f,
		-1.0f,	+1.0f,	-1.0f,	0.8f,	0.2f,	0.2f,
		-1.0f,	-1.0f,	+1.0f,	0.8f,	0.2f,	0.2f,
		-1.0f,	-1.0f,	+1.0f,	0.8f,	0.2f,	0.2f,
		-1.0f,	+1.0f,	-1.0f,	0.8f,	0.2f,	0.2f,
		-1.0f,	-1.0f,	-1.0f,	0.8f,	0.2f,	0.2f,
		// Face x+
		+1.0f,	+1.0f,	+1.0f,	0.8f,	0.2f,	0.2f,
		+1.0f,	-1.0f,	+1.0f,	0.8f,	0.2f,	0.2f,
		+1.0f,	+1.0f,	-1.0f,	0.8f,	0.2f,	0.2f,
		+1.0f,	+1.0f,	-1.0f,	0.8f,	0.2f,	0.2f,
		+1.0f,	-1.0f,	+1.0f,	0.8f,	0.2f,	0.2f,
		+1.0f,	-1.0f,	-1.0f,	0.8f,	0.2f,	0.2f,
		// Face y-
		+1.0f,	-1.0f,	+1.0f,	0.2f,	0.8f,	0.2f,
		-1.0f,	-1.0f,	+1.0f,	0.2f,	0.8f,	0.2f,
		+1.0f,	-1.0f,	-1.0f,	0.2f,	0.8f,	0.2f,
		+1.0f,	-1.0f,	-1.0f,	0.2f,	0.8f,	0.2f,
		-1.0f,	-1.0f,	+1.0f,	0.2f,	0.8f,	0.2f,
		-1.0f,	-1.0f,	-1.0f,	0.2f,	0.8f,	0.2f,
		// Face y+
		+1.0f,	+1.0f,	+1.0f,	0.2f,	0.8f,	0.2f,
		+1.0f,	+1.0f,	-1.0f,	0.2f,	0.8f,	0.2f,
		-1.0f,	+1.0f,	+1.0f,	0.2f,	0.8f,	0.2f,
		-1.0f,	+1.0f,	+1.0f,	0.2f,	0.8f,	0.2f,
		+1.0f,	+1.0f,	-1.0f,	0.2f,	0.8f,	0.2f,
		-1.0f,	+1.0f,	-1.0f,	0.2f,	0.8f,	0.2f,
		// Face z-
		+1.0f,	+1.0f,	-1.0f,	0.2f,	0.2f,	0.8f,
		+1.0f,	-1.0f,	-1.0f,	0.2f,	0.2f,	0.8f,
		-1.0f,	+1.0f,	-1.0f,	0.2f,	0.2f,	0.8f,
		-1.0f,	+1.0f,	-1.0f,	0.2f,	0.2f,	0.8f,
		+1.0f,	-1.0f,	-1.0f,	0.2f,	0.2f,	0.8f,
		-1.0f,	-1.0f,	-1.0f,	0.2f,	0.2f,	0.8f,
		// Face z+
		+1.0f,	+1.0f,	+1.0f,	0.2f,	0.2f,	0.8f,
		-1.0f,	+1.0f,	+1.0f,	0.2f,	0.2f,	0.8f,
		+1.0f,	-1.0f,	+1.0f,	0.2f,	0.2f,	0.8f,
		+1.0f,	-1.0f,	+1.0f,	0.2f,	0.2f,	0.8f,
		-1.0f,	+1.0f,	+1.0f,	0.2f,	0.2f,	0.8f,
		-1.0f,	-1.0f,	+1.0f,	0.2f,	0.2f,	0.8f
	};

	GLuint vertBufferID;
	glGenBuffers(1, &vertBufferID);
	glBindBuffer(GL_ARRAY_BUFFER, vertBufferID);
	glBufferData(GL_ARRAY_BUFFER, sizeof(cubeVerts), cubeVerts, GL_STATIC_DRAW);
	GLint posID = glGetAttribLocation(program.GetPID(), "position");
	glEnableVertexAttribArray(posID);
	glVertexAttribPointer(posID, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), 0);
	GLint colID = glGetAttribLocation(program.GetPID(), "color");
	glEnableVertexAttribArray(colID);
	glVertexAttribPointer(colID, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void *)(3 * sizeof(float)));

}

void FrameBufferSizeCallback(GLFWwindow* lWindow, int width, int height)
{
	glViewport(0, 0, width, height);
}

void Init()
{
	glfwInit();
	glfwWindowHint(GLFW_COCOA_RETINA_FRAMEBUFFER, GL_FALSE);
	window = glfwCreateWindow(WINDOW_WIDTH, WINDOW_HEIGHT, "Assignment2 - <Your Name>", NULL, NULL);
	glfwMakeContextCurrent(window);
	glewExperimental = GL_TRUE;
	glewInit();
	glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT);
	glfwSetMouseButtonCallback(window, MouseCallback);
	glfwSetCursorPosCallback(window, CursorPositionCallback);
	glfwSetCharCallback(window, CharacterCallback);
	glfwSetFramebufferSizeCallback(window, FrameBufferSizeCallback);
	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
	glEnable(GL_DEPTH_TEST);
	glfwSetScrollCallback(window, ScrollCallback);

	program.SetShadersFileName(resource_path + "shader.vert", resource_path + "shader.frag");
	program.Init();

	CreateCube();

	torso.addChild(&head);

	torso.addChild(&upperRightArm);
	upperRightArm.addChild(&lowerRightArm);

	torso.addChild(&upperLeftArm);
	upperLeftArm.addChild(&lowerLeftArm);

	torso.addChild(&upperRightLeg);
	upperRightLeg.addChild(&lowerRightLeg);

	torso.addChild(&upperLeftLeg);
	upperLeftLeg.addChild(&lowerLeftLeg);

	torso.getTraversal(traversal);
	traversal[selectedIdx]->setSelected(true);
}


int main(int argc, char *argv[])
{	
	if (argc < 2)
	{
		std::cout << "Need to specify the resource path as the input argument." << std::endl;
		return 0;
	}
	else
		resource_path = argv[1];

	Init();
	while ( glfwWindowShouldClose(window) == 0) 
	{
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		Display();
		glFlush();
		glfwSwapBuffers(window);
		glfwPollEvents();
	}

	glfwTerminate();
	return 0;
}
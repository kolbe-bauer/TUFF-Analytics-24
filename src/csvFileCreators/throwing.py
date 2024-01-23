from Enums.throw import (ThrowForce, ThrowType, ThrowSubtype, ThrowOutcome, ThrowDecision, ThrowAspirations,
                         ComingOutOfTimeout)


class Throwing:
    def __init__(self, action_beginner, action_ender, force: ThrowForce, throw_subtype: ThrowSubtype,
                 throw_type: ThrowType, throw_aspirations: ThrowAspirations, timeout: ComingOutOfTimeout,
                 throw_decision: ThrowDecision, throw_outcome: ThrowOutcome):
        self.action_beginner = action_beginner
        self.action_ender = action_ender
        self.force = force
        self.throw_subtype = throw_subtype
        self.throw_type = throw_type
        self.throw_aspirations = throw_aspirations
        self.timeout = timeout
        self.throw_decision = throw_decision
        self.throw_outcome = throw_outcome

    def get_action_beginner(self):
        return self.action_beginner

    def set_action_beginner(self, value):
        self.action_beginner = value

    def get_action_ender(self):
        return self.action_ender

    def set_action_ender(self, value):
        self.action_ender = value

    def get_force(self):
        return self.force

    def set_force(self, value):
        self.force = value

    def get_throw_subtype(self):
        return self.throw_subtype

    def set_throw_subtype(self, value):
        self.throw_subtype = value

    def get_throw_type(self):
        return self.throw_type

    def set_throw_type(self, value):
        self.throw_type = value

    def get_throw_aspirations(self):
        return self.throw_aspirations

    def set_throw_aspirations(self, value):
        self.throw_aspirations = value

    def get_timeout(self):
        return self.timeout

    def set_timeout(self, value):
        self.timeout = value

    def get_throw_decision(self):
        return self.throw_decision

    def set_throw_decision(self, value):
        self.throw_decision = value
